import wx
from view.main_frame import MainFrame


class PasswordManagerApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame()
        self.frame.Show()
        return True


if __name__ == "__main__":
    app = PasswordManagerApp()
    app.MainLoop()
