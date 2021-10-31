# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

from main import sqliteCRUD_HW

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Blood Donor Administration System ", pos = wx.DefaultPosition, size = wx.Size( 350,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        # self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Id", wx.Point( -1,-1 ), wx.Size( 90,-1 ), 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer6.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtId = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,-1 ), wx.TE_RIGHT )
        self.txtId.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer6.Add( self.txtId, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
        
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
        self.m_staticText2.Wrap( -1 )
        self.m_staticText2.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer7.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,-1 ), wx.TE_RIGHT )
        self.txtName.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer7.Add( self.txtName, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer7, 1, wx.EXPAND, 5 )
        
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Age", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
        self.m_staticText3.Wrap( -1 )
        self.m_staticText3.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer8.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtAge = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,-1 ), wx.TE_RIGHT )
        self.txtAge.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer8.Add( self.txtAge, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer9.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtGender = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,-1 ), wx.TE_RIGHT )
        self.txtGender.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer9.Add( self.txtGender, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"BloodType", wx.DefaultPosition, wx.Size( 90,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer10.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.txtBloodType = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,-1 ), wx.TE_RIGHT )
        self.txtBloodType.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer10.Add( self.txtBloodType, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,1 ), 0 )
        self.m_staticText16.Wrap( -1 )
        bSizer2.Add( self.m_staticText16, 0, wx.ALL, 5 )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Remark", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.txtRemark = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,50 ), wx.TE_LEFT|wx.TE_MULTILINE )
        bSizer2.Add( self.txtRemark, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button5 = wx.Button( self, wx.ID_ANY, u"Registration", wx.DefaultPosition, wx.Size( 105,-1 ), wx.NO_BORDER|wx.NO_BORDER )
        self.m_button5.SetFont( wx.Font( 9, 70, 90, 90, False, "Consolas" ) )
        self.m_button5.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        
        bSizer3.Add( self.m_button5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_button6 = wx.Button( self, wx.ID_ANY, u"Modification", wx.DefaultPosition, wx.Size( 105,-1 ), wx.NO_BORDER|wx.NO_BORDER )
        self.m_button6.SetFont( wx.Font( 9, 70, 90, 90, False, "Consolas" ) )
        self.m_button6.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        
        bSizer3.Add( self.m_button6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_button7 = wx.Button( self, wx.ID_ANY, u"Deletion", wx.DefaultPosition, wx.Size( 105,-1 ), wx.NO_BORDER|wx.NO_BORDER )
        self.m_button7.SetFont( wx.Font( 9, 70, 90, 90, False, "Consolas" ) )
        self.m_button7.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        
        bSizer3.Add( self.m_button7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_button10 = wx.Button( self, wx.ID_ANY, u"InfoInquiry", wx.DefaultPosition, wx.Size( 160,-1 ), wx.NO_BORDER|wx.NO_BORDER )
        self.m_button10.SetFont( wx.Font( 9, 70, 90, 90, False, "Consolas" ) )
        self.m_button10.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        
        bSizer4.Add( self.m_button10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        self.m_button11 = wx.Button( self, wx.ID_ANY, u"AllInfoInquiry", wx.DefaultPosition, wx.Size( 160,-1 ), wx.NO_BORDER|wx.NO_BORDER )
        self.m_button11.SetFont( wx.Font( 9, 70, 90, 90, False, "Consolas" ) )
        self.m_button11.SetBackgroundColour( wx.Colour( 200, 200, 200 ) )
        
        bSizer4.Add( self.m_button11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Work History", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        self.m_staticText7.Wrap( -1 )
        self.m_staticText7.SetFont( wx.Font( 13, 70, 90, 90, False, "Consolas" ) )
        
        bSizer5.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.ResultArea = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,150 ), wx.HSCROLL|wx.TE_LEFT|wx.TE_MULTILINE )
        bSizer5.Add( self.ResultArea, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer5, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.m_button5.Bind( wx.EVT_BUTTON, self.OnInsert )
        self.m_button6.Bind( wx.EVT_BUTTON, self.OnUpdate )
        self.m_button7.Bind( wx.EVT_BUTTON, self.OnDelete )
        self.m_button10.Bind( wx.EVT_BUTTON, self.OnSelect )
        self.m_button11.Bind( wx.EVT_BUTTON, self.OnSelectAll )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnInsert( self, event ):
        id = self.txtId.GetValue()
        name = self.txtName.GetValue()
        age = self.txtAge.GetValue()
        gender = self.txtGender.GetValue()
        bloodtype = self.txtBloodType.GetValue()
        remark = self.txtRemark.GetValue()

        try:
            sqliteCRUD_HW.insertData(id, name, age, gender, bloodtype, remark)
            self.ResultArea.AppendText('> ' + id + '번 - ' + name + '님 정보 등록완료.\n')
            
        except:
            print('예외발생!')
        
        finally:
            print('입력작업 종료')
        
        event.Skip()
    
    def OnUpdate( self, event ):
        id = self.txtId.GetValue()
        name = self.txtName.GetValue()
        age = self.txtAge.GetValue()
        gender = self.txtGender.GetValue()
        bloodtype = self.txtBloodType.GetValue()
        remark = self.txtRemark.GetValue()

        try:
            sqliteCRUD_HW.update((name, age, gender, bloodtype, remark, id))
            self.ResultArea.AppendText('> ' + id + '번 - ' + name + '님 정보 수정완료.\n')
            
        except:
            print('예외발생!')
        
        finally:
            print('입력작업 종료')
        
        event.Skip()
    
    def OnDelete( self, event ):
        id = self.txtId.GetValue()
        name = self.txtName.GetValue()
        res = sqliteCRUD_HW.delete(id)
        
        self.ResultArea.AppendText('> ' + id + '번 - ' + name + '님 정보 삭제완료.\n')
        
        
        event.Skip()
    
    def OnSelect( self, event ):
        key = self.txtId.GetValue()
        row = sqliteCRUD_HW.select(key)
        
        self.txtId.SetValue(row[0])
        self.txtName.SetValue(row[1])
        self.txtAge.SetValue(row[2])
        self.txtGender.SetValue(row[3])
        self.txtBloodType.SetValue(row[4])
        self.txtRemark.SetValue(row[5])
        
        self.ResultArea.AppendText('> ' + row[0] + '번 - ' + row[1] + '님 조회완료.\n')
        
        event.Skip()
    
    def OnSelectAll( self, event ):
        rows = sqliteCRUD_HW.selectAll()
        
        self.ResultArea.AppendText('-----------------이하 전체 데이터 표시-----------------\n')
        
        for row in rows:
            self.ResultArea.AppendText('{}, {}, {}, {}, {}, {}\n'.format(row[0],row[1],row[2],row[3],row[4],row[5]))
        
        self.ResultArea.AppendText('-----------------모든 데이터 조회완료.-----------------\n')
        
        event.Skip()
    

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    
    app.MainLoop()    
    
    pass