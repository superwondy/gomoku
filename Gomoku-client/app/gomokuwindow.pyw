#!/usr/bin/env python
# -*- coding: utf-8 -*-
#======================================================================
#
# gomokuwindow.py - network data stream operation interface
#
# NOTE: 游戏窗口类 
#                                                                                                                                                                        
#======================================================================
import time
import json
import logging
import threading
import random

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QRectF
from PyQt4.QtGui import QPixmap, QGraphicsScene, QGraphicsPixmapItem
from ui.ui_mainPannel import Ui_mainPannel
from client import GomokuClient
from lib.service import service
import lib.log as log
import lib.datatag as dtag


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

#======================================================================
# 头定义数据
#======================================================================
PANNEL_ROW              = 15
PANNEL_COLUMN           = 15
PANNEL_START_X          = 222
PANNEL_START_Y          = 133
PANNEL_END_X            = 688
PANNEL_END_Y            = 595
PANNEL_OFFSET           = 5
OFFSET                  = 32
HALF_OFFSET             = 16

#游戏状态信息
GAME_REDEAY             = 1
GAME_START              = 2
GAME_HOLD_UP            = 3
GAME_PLAYING            = 4
GAME_WAITING            = 5
GAME_STOP               = 6
GAME_IN_TURN            = 7

logger = log.get_logger('GomokuWindow')
#======================================================================
# GomokuWindow 游戏面板类
#======================================================================
class GomokuWindow(QtGui.QMainWindow, Ui_mainPannel, service):
    """docstring for GomokuWindow"""
    # SERVICE_ID = random.randint(10000, 40000)
    global logger
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        service.__init__(self)
        # service.__init__(self, self.__class__.SERVICE_ID)
        self.setWindowFlags(Qt.Window|Qt.FramelessWindowHint)
        self.setupUi(self)

        self.__init_ui()
        self._init_attr()
        pass

    #----------------------------------------------------------------------
    # 类属性设置
    #----------------------------------------------------------------------
    def _init_attr(self):
        commands = {
            dtag.MOVE:              self.handle_opponent_move,
            dtag.BACK_MOVE:         self.handle_opponent_back_move,
            dtag.BACK_MOVE_REPLY:   self.handle_back_move_reply,
            dtag.PLAYER_CHAT:       self.handle_chat_msg,
            dtag.GAME_WIN:          self.handle_win,
            dtag.GAME_STATE:        self.handle_game_state,
            dtag.USER_INFO_REPLY:   self.handle_user_info_reply
        }
        
        self.client = None
        self.username = 'user'
        self.hid = 11
        self.opponent_hid = 22
        self.room_id = None
        self.table_id = None
        self.seat_id = None
        self.flag_color = None
        self.opponent_flag_color = None
        # self.shutdown = False
        self.panel = [[0 for col in range(PANNEL_COLUMN)] for row in range(PANNEL_ROW)]

        # 游戏状态信息
        self.game_state = GAME_WAITING

        # 游戏结果弹框
        self.dialog = None

        # 保存大厅对象
        self.groom = None

        # 保存棋子(item, x, y)
        self.flags = []
        self.curr_flag = None
        self.opponent_curr_flag = None

        self.registers(commands)

    # 初始化界面
    def __init_ui(self):
        self.isOnDrag = False
        self.scene = QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/image/playtable.png")))
        self.graphicsView.setScene(self.scene)
        self.pannelHeader.setPixmap(QtGui.QPixmap(_fromUtf8(":/image/image/pannelheader.png")))

        # 玩家头像
        lp = QPixmap(_fromUtf8(":/image/image/rplayer.jpg"))
        self.lPlayer.setPixmap(lp.scaled(self.lPlayer.width(),self.lPlayer.height(),Qt.KeepAspectRatio))
        rp = QPixmap(_fromUtf8(":/image/image/rplayer.jpg"))
        self.rPlayer.setPixmap(lp.scaled(self.rPlayer.width(),self.rPlayer.height(),Qt.KeepAspectRatio))
        
        # # 黑子和白子
        # bp = QPixmap(_fromUtf8(":/icon/icon/blackplayer.png"))
        # self.labelblack.setPixmap(bp.scaled(self.labelblack.width(),self.labelblack.height(),Qt.KeepAspectRatio))
        # wp = QPixmap(_fromUtf8(":/icon/icon/whiteplayer.png"))
        # self.labelwhite.setPixmap(wp.scaled(self.labelwhite.width(),self.labelwhite.height(),Qt.KeepAspectRatio))
        # # 轮到下棋玩家
        # pp = QPixmap(_fromUtf8(":/icon/icon/player.png"))
        # self.labelInTurn.setPixmap(pp.scaled(self.labelInTurn.width(),self.labelInTurn.height(),Qt.KeepAspectRatio))  
        
        self.btDrawGame.hide()
        self.setup_action()

    # 设置棋子颜色
    def set_flag_color(self):
        if self.seat_id == 1:
            self.flag_color = ":/image/image/white.png"
            self.opponent_flag_color = ":/image/image/black.png"

            self.cur_flag_color = ":/image/image/sticwhite.png"
            self.cur_opponent_flag_color = ":/image/image/sticblack.png"
        else:
            self.flag_color = ":/image/image/black.png"
            self.opponent_flag_color = ":/image/image/white.png"

            self.cur_flag_color = ":/image/image/sticblack.png"
            self.cur_opponent_flag_color = ":/image/image/sticwhite.png"

    # 设置自己的房间，桌子，座位号
    def set_room_table_seat(self, room, table, seat):
        self.room_id = room
        self.table_id = table
        self.seat_id = seat
        self.set_flag_color()

    # 保存大厅窗口类
    def set_parent(self, parent=None):
        if parent:
            self.groom = parent
        return parent

    # 设置用户名
    def set_user_name(self, name):
        self.username = name

    # 设置消息代理
    def set_client(self, client):
        self.client = client

    #----------------------------------------------------------------------
    # 服务端信息同步处理
    #----------------------------------------------------------------------

    # 对方下一步子
    def handle_opponent_move(self, jdata):
        x = jdata[u'row']
        y = jdata[u'column']
        logger.debug(str(self.SID) + ', 对方移动一步：(' + str(x) + ',' + str(y) + ')')
        item = QGraphicsPixmapItem(QPixmap(_fromUtf8(self.cur_opponent_flag_color)))
        item.setPos(PANNEL_OFFSET+OFFSET*x,PANNEL_OFFSET+OFFSET*y)
        if self.opponent_curr_flag:
            self.opponent_curr_flag.setPixmap(QPixmap(_fromUtf8(self.opponent_flag_color)))
        self.scene.addItem(item)
        self.opponent_curr_flag = item
        self.flags.append((item, x, y))

        self.panel[x][y] = self.opponent_hid
        logger.debug('桌面棋子数: ' + str(len(self.scene.items())))

        #对方下子位置
        pos = '对方下子位置：' + str(x) + "x" + str(y) + '\n'
        #轮到自己下子
        self.labelInTurn.setParent(self.groupBoxL)
        self.labelInTurn.setGeometry(QtCore.QRect(135, 170, 52, 31))
        self.game_state = GAME_IN_TURN
        self.labelState.setText(_fromUtf8( pos + '该你下子了'))

    # 对方悔棋
    def handle_opponent_back_move(self, jdata):
        reply = QtGui.QMessageBox.question(self, 'Message',
            _fromUtf8('对方申请悔棋，答应吗？'), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        data = {}
        data['tag'] = dtag.BACK_MOVE_REPLY
        if reply == QtGui.QMessageBox.Yes:
            data['reply'] = True
            self.game_state = GAME_WAITING
            self.labelState.setText(_fromUtf8('该对方下子'))
        else:
            data['reply'] = False
        self.client.send(json.dumps(data))
        self.back_move()
        logger.debug('handle_opponent_back_move' + json.dumps(jdata))

    def handle_back_move_reply(self, jdata):
        reply = jdata['reply']
        if reply:
            self.back_move()
            print '对方同意悔棋！'
            self.game_state = GAME_IN_TURN
            self.labelState.setText(_fromUtf8( pos + '该你下子了'))
        else:
            print '对方不同意悔棋！'
            reply = QtGui.QMessageBox.warning(self, 'Message', \
                _fromUtf8('不好意思，对手不同意悔棋'))


    # 对方发来一条聊天信息
    def handle_chat_msg(self, jdata):
        msg = unicode(self.editMsg.toPlainText())
        # if len(msg) > 1024:
        #     msg = msg[1024/2:]
        msg = msg + jdata['user'] + ': ' + jdata['msg'] + '\n'
        self.editMsg.setText(_fromUtf8(msg))
        logger.debug('对方发来一条消息')

    # 游戏输赢情况
    def handle_win(self, jdata):
        result = unicode(jdata['result']).encode('utf-8')
        text = self.username + ', '

        if result == 'win':
            if jdata['lose']:
                text += '对方掉线\n'
            text += '恭喜你，赢啦！\n 邀请对方再玩一次？'
        elif result == 'lose':
            if jdata['lose']:
                text += '你掉线啦！\n'
            text += '很抱歉，你输啦！\n 重新开始游戏？'

        elif result == 'giveup':
            text += '对方认输！\n'

        reply = QtGui.QMessageBox.question(self, 'Message',
            _fromUtf8(text), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        self.game_state = GAME_STOP
        self.labelState.setText(_fromUtf8('游戏结束！'))
        if reply == QtGui.QMessageBox.Yes:
            self.reset_game()
            self.game_state = GAME_REDEAY
            self.notion_state()
        else:
            pass
        logger.debug('输赢信息提示：' + result.encode('utf-8'))

    # 游戏状态更新
    def handle_game_state(self, jdata):
        logger.debug('更新游戏状态' + json.dumps(jdata))
        state = jdata['state']
        if state == GAME_START:
            self.labelrightuser.setText(_fromUtf8(jdata['op_name']))
            self.rightEditvectory.setText(_fromUtf8(str(jdata['op_score'])))
        self.update_state(state)

    def handle_user_info_reply(self, jdata):
        luser = unicode(self.labelleftuser.text())
        ruser = unicode(self.labelrightuser.text())
        name = jdata['name']
        if luser == name:
            self.leftEditvectory.setText(jdata['score'])
        else:
            self.rightEditvectory.setText(jdata['score'])

    #----------------------------------------------------------------------
    # 状态更新处理
    #----------------------------------------------------------------------

    # 更新状态
    def update_state(self, state):
        self.notion_state(state)
        if state in (GAME_START, GAME_REDEAY):
            self.game_state = GAME_IN_TURN
        elif state == GAME_PLAYING:
            pass

    # 更新状态面板
    def notion_state(self, state):
        if state == GAME_PLAYING:
            self.labelState.setText(_fromUtf8('游戏中'))
            self.btGameStart.setText(_fromUtf8('暂停'))
        elif state == GAME_WAITING:
            self.labelState.setText(_fromUtf8('该对方下子'))
        elif state == GAME_START:
            self.btGameStart.setText(_fromUtf8('暂停'))
            self.labelState.setText(_fromUtf8('游戏可以开始'))
        elif state == GAME_REDEAY:
            self.btGameStart.setText(_fromUtf8('已准备'))

    # 双方各回退一个棋子
    def back_move(self):
        step = 1
        while step > 0:
            step -= 1
            item, x, y = self.flags.pop()
            self.scene.removeItem(item)
            self.panel[x][y] = 0

    def leave_game(self):
        self.game_state = GAME_WAITING
        self.update_state(state)

        self.reset_game()
        jdata = {}
        jdata['tag'] = dtag.GAME_LEAVE
        self.client.send(json.dumps(jdata))

    # 重置游戏
    def reset_game(self):
        while len(self.flags) != 0:
            item, x, y = self.flags.pop()
            self.scene.removeItem(item)
            self.panel[x][y] = 0


    #----------------------------------------------------------------------
    # 控件点击事件处理
    #----------------------------------------------------------------------

    # 开始游戏
    def bt_game_start(self):
        self.notion_state(self.game_state)

    # 发送聊天信息
    def bt_send_msg(self):
        text = unicode(self.lineMsg.text())
        jdata = {}
        jdata['tag'] = dtag.PLAYER_CHAT
        jdata['user'] = self.username
        jdata['msg'] = text.encode('utf-8')
        self.client.send_chat_msg(jdata)
        msg = unicode(self.editMsg.toPlainText())
        # if len(msg) > 1024:
        #     msg = msg[1024/2:]
        msg = msg + u'我:' + text + '\n'
        self.editMsg.setText(_fromUtf8(msg))
        self.lineMsg.setText('')

    # 悔棋
    def bt_back_move(self):
        jdata = {}
        jdata['tag'] = dtag.BACK_MOVE
        self.client.send(json.dumps(jdata))

    # 申请和棋
    def bt_draw_move(self):
        pass

    # 认输
    def bt_give_up(self):
        jdata = {}
        jdata['tag'] = dtag.GAME_GIVE_UP
        self.client.send(json.dumps(jdata))
        self.reset_game()

    # 关闭游戏窗口
    def bt_close_window(self):
        if self.groom:
            self.groom.showNormal()
        self.reset_game()

        jdata = {}
        jdata['tag'] = dtag.GAME_LEAVE
        self.client.send(json.dumps(jdata))

        self.hide()

    # 设置界面响应事件
    def setup_action(self):
        self.btGameStart.clicked.connect(self.bt_game_start)
        self.btSendMsg.clicked.connect(self.bt_send_msg)
        self.lineMsg.returnPressed.connect(self.bt_send_msg)
        self.btBackmove.clicked.connect(self.bt_back_move)
        self.btDrawGame.clicked.connect(self.bt_draw_move)
        self.btGiveUp.clicked.connect(self.bt_give_up)
        self.btClose.clicked.connect(self.bt_close_window)

    # 自己下一步子
    def playe_one_move(self, x, y):
        x = x - PANNEL_START_X
        y = y - PANNEL_START_Y
        p_x = x / OFFSET
        p_y = y / OFFSET
        f_x = x % OFFSET
        f_y = y % OFFSET
        if HALF_OFFSET < f_x: p_x += 1
        if HALF_OFFSET < f_y: p_y += 1
        if self.panel[p_x][p_y] != 0:
            print self.panel
            print self.panel[p_x][p_y]
            logger.debug(_fromUtf8('没有空位，不能在这下子：(' + str(p_x) + ', ' + str(p_y) + ')'))
            return
        item = QGraphicsPixmapItem(QPixmap(_fromUtf8(self.cur_flag_color)))
        item.setPos(PANNEL_OFFSET+OFFSET*p_x,PANNEL_OFFSET+OFFSET*p_y)
        if self.curr_flag:
            self.curr_flag.setPixmap(QPixmap(_fromUtf8(self.flag_color)))
        self.scene.addItem(item)
        self.curr_flag = item
        self.flags.append((item, p_x, p_y))

        #发送同步给对手
        jdata = {}
        jdata['tag'] = dtag.MOVE
        jdata['row'] = p_x
        jdata['column'] = p_y
        self.client.send(json.dumps(jdata))
        self.panel[p_x][p_y] = self.hid
        logger.debug('自己下一棋：(' + str(p_x) + ', ' + str(p_y) + ')')

        #轮到对方下
        self.labelInTurn.setParent(self.groupBoxR)
        self.labelInTurn.setGeometry(QtCore.QRect(10, 170, 52, 31))
        self.game_state = GAME_WAITING
        self.labelState.setText(_fromUtf8('该对方下子'))


    #----------------------------------------------------------------------
    # 鼠标事件处理
    #----------------------------------------------------------------------
    def mouseMoveEvent(self, event):
        if self.isOnDrag:
            self.move(event.globalPos()-self.dragPosition)

    def mousePressEvent(self, event):
        print event.pos()
        if event.button() == Qt.LeftButton:
            x = event.x()
            y = event.y()
            self.dragPosition = event.globalPos() - self.pos()
            if self.dragPosition.y() <= 40:
                self.isOnDrag = True
            elif x > PANNEL_START_X and x < PANNEL_END_X \
                    and y > PANNEL_START_Y and y < PANNEL_END_Y:
                if self.game_state != GAME_IN_TURN:
                    self.notion_state(self.game_state)
                    return
                self.playe_one_move(x, y)

    def mouseReleaseEvent(self, event):
        self.isOnDrag = False

    def opponent_move(self, jdata):
        x = jdata['row']
        y = jdata['column']
        item = QGraphicsPixmapItem(QPixmap(_fromUtf8(self.opponent_flag_color)))
        item.setPos(PANNEL_OFFSET+OFFSET*x,PANNEL_OFFSET+OFFSET*y)
        self.scene.addItem(item)

if __name__ == '__main__':
        import sys
        app = QtGui.QApplication(sys.argv)
        app.setApplicationName("GomokuWindow Pannel")
        app.setQuitOnLastWindowClosed(True)

        window = GomokuWindow()
        window.show()
        sys.exit(app.exec_())
