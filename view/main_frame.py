import wx
from controller.password_controller import PasswordController

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None)
        self.panel = MainPanel(self)
        self.SetTitle("Password Manager")
        self.SetSize(800, 600)

class MainPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = PasswordController()
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.make_password_creation_ctrl()
        self.make_search_text_ctrl()
        self.make_display_sites()

        self.SetSizer(self.main_sizer)

    def make_search_text_ctrl(self) -> None:
        #display
        self.search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.search_text_ctrl = wx.TextCtrl(self)
        self.validate_search_btn = wx.Button(self, label = "Search")
        
        self.search_sizer.Add(self.search_text_ctrl, wx.ALL | wx.EXPAND, 4)
        self.search_sizer.Add(self.validate_search_btn, wx.ALL | wx.EXPAND, 4)
        #event definition
        self.Bind(wx.EVT_BUTTON, self.__on_search, self.validate_search_btn)

        #adding to main sizer
        self.main_sizer.Add(self.search_sizer, wx.ALL | wx.EXPAND | wx.TOP | wx.BOTTOM, 4)
        

    def make_display_sites(self) -> None:
        self.site_list = wx.ListCtrl(self, style = wx.LC_REPORT)
        self.site_list.AppendColumn("Sites")
        sites = self.controller.get_sites()

        self.__refresh_site_display(sites)
        
        self.main_sizer.Add(self.site_list, wx.ALL | wx.EXPAND, 4)

    def make_password_creation_ctrl(self) -> None:
        #display
        self.password_creation_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.password_creation_ctrl = wx.TextCtrl(self)
        self.save_btn = wx.Button(self, label = "Save")

        self.password_creation_sizer.Add(self.password_creation_ctrl, wx.ALL | wx.EXPAND, 4)
        self.password_creation_sizer.Add(self.save_btn, wx.ALL | wx.EXPAND, 4)

        #event definition
        self.Bind(wx.EVT_BUTTON, self.__on_save, self.save_btn)

        #adding to main sizer
        self.main_sizer.Add(self.password_creation_sizer, wx.ALL | wx.EXPAND | wx.TOP | wx.BOTTOM, 4)

    #handlers
    def __on_save(self, event) -> None:
        site = self.password_creation_ctrl.Value
        if site != "":
            self.controller.create_password(site)
            sites = self.controller.get_sites()
            self.__refresh_site_display(sites)

    def __on_search(self, event) -> None:
        sites = self.controller.search_site(self.search_text_ctrl.Value)
        self.__refresh_site_display(sites)

    #private func
    def __refresh_site_display(self, sites) -> None:
        self.site_list.ClearAll()
        self.site_list.AppendColumn("Sites")

        if len(sites) == 0:
            self.site_list.Append(["No site found."])
        else:
            for site in sites:
                self.site_list.Append([site])
