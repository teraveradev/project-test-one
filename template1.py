navigation_helper = """
Screen:
 MDNavigationLayout:
  MDScreenManager:
   Screen:
    
    MDBoxLayout:
     orientation: "vertical"
     MDTopAppBar:
      type:"top"
      padding : 10
      spacing: -20
      left_action_items: [["account-badge-outline", lambda x: profil_bar.set_state("toggle")]] 

      MDTextField:
       hint_text:'What are you looking for'
       pos_hint: {'center_x':0.5,'center_y':0.5}
       icon_right:"home-search-outline"
       size_hint_x:None
       width:250
       mode:"round"
       hint_text_color_normal: "pink"
       hint_text_color_focus: "pink"
       text_color_normal: "pink"
       text_color_focus: "pink"
      
    


     

      
     MDBottomNavigation:

      MDBottomNavigationItem:
       name: "screen 1"  
       icon: "home-city"
       MDLabel:
        text:"homefeed"
        halign:"center"

      MDBottomNavigationItem:
       name: "paperclip "
       icon: "message"
       MDLabel:
        text:"script"
        halign:"center"

      MDBottomNavigationItem:
       name: "screen 3"
       icon: "account-supervisor-outline"
       MDLabel:
        text:"freelance research"
        halign:"center"

      MDBottomNavigationItem:
       name: "screen 4"
       icon: "gift"
       MDLabel:
        text:"gift"
        halign:"center"

      
       

  MDNavigationDrawer:
   id: profil_bar
  
  """