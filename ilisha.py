import serial
import time
from dynamixel_sdk import *

class Ilusha(object):

    PROTOCOL_VERSION = 1.0

    """docstring forIlusha."""

    def __init__(self, portHandler, id):
        super(Ilusha, self).__init__()
        self.portHandler = portHandler
        self.packetHandler = PacketHandler(self.PROTOCOL_VERSION)
        self.id = id

    def write2byte(self, addres, data):
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, self.id , addres, data)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))

    def write1byte(self, addres, data):
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, self.id , addres, data)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))

    def read2byte(self, addres):
        a, dxl_comm_result, dxl_error = self.packetHandler.read2ByteTxRx(self.portHandler, self.id, addres)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
        return a

    def read1byte(self, addres):
        a, dxl_comm_result, dxl_error = self.packetHandler.read1ByteTxRx(self.portHandler, self.id, addres)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % self.packetHandler.getRxPacketError(dxl_error))
        return a


    def set_enable(self, enable):
        self.write1byte(24, enable)

    def set_PID_P(self, p):
        self.write1byte(28, p)

    def set_PID_I(self, i):
        self.write1byte(27, i)

    def set_PID_D(self, d):
        self.write1byte(26, d)

    def set_max_pwm(self, pwm):
        self.write2byte(14, pwm)

    def set_max_pwm_inc(self, pwm):
        self.write1byte(16, pwm)

    def set_angle(self, angle):
        self.write2byte(30, angle)
        
    def set_angle_offset(self, angle):
        self.write2byte(20, angle)

    def get_angle(self):
        return self.read2byte(36)
        
    def get_goal_angle(self):
        return self.read2byte(30)

    def get_current(self):
        return self.read2byte(40)

    def get_volts(self):
        return self.read1byte(42)
