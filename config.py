# config for the project

window_title = "Mini POS System (by CS311 Project @ BU)"
window_logo = "assets\\backend\\images\\pos_logo_64.ico"
window_width = 1280
window_height = 720
window_resizeable = False
window_background_color = '#205375'
window_background_color2 = '#2C6489'
color_black = '#000000'
color_white = '#FFFFFF'
color_red = '#D82148'
color_green = '#00C853'
color_default = '#EFEFEF'
color_default_dark = '#c4c4c4'
color_highlight = '#F66B0E'
color_list_odd = '#FFFFFF'
color_list_even = '#E5E5E5'
color_list_selected = '#606060'
# color? = '#112B3C'

def calculate_number():
    pass

cart = []

if __name__ == '__main__':
    import main
    main.App()