# coding=utf-8
import cv2 as cv


class PictureActions:

    """###############################################################
    # FUNCTION NAME: __init__                                        #
    # DESCRIPTION: only on creating an instance of PictureActions    #
    # ARGUMENTS: window(optional)                                    #
    #                                                                #
    # ARGUMENT    TYPE            DESCRIPTION                        #
    # window      WindowActions   the window the instance belongs to #
    #                                                                #
    # RETURNS:                                                       #
    ###############################################################"""
    def __init__(self, window=None):
        """
        # window=None Bedeutung:
        # Bei einer Methode kann man bekanntlich Parameter(Übergabewerte) definieren, die beim Methodenaufruf #
        # ZWINGEND erforderlich sind. --> Beispiel: def addiere(self, zahl1, zahl2)                           #
        #                                           Instanz.addiere(1, 2)                                     #
        # Möchte man eine Methode haben, die beim Methodenaufruf einen Parameter haben KANN dann macht man    #
        # dies mittels parameter=None --> Beispiel: def neuerTermin(self, uhrzeit, spezielle_kleidung=None)   #
        #                                    (1)    Instanz.neuerTermin(18:00, Anzug)                         #
        #                                    (2)    Instanz.neuerTermin(19:00)                                #
        # Bei (1) wird ein Termin erstellt und der Parameter spezielle_kleidung hat den Wert Anzug            #
        # Bei (2) wird ein Termin erstellt und der Parameter spezielle_kleidung erhält den Wert None          #
        #                               Anmerkung:                                                            #
        # Es können auch andere Werte als None definiert werden:                                              #
        # def addiere(zahl1, zahl2=5)                                                                         #
        # def schreiben(Text="Hallo")                                                                         #
        """

        """
        Wird ausgeführt wenn eine Instanz (ein Objekt) der Klasse PictureActions erstellt wird
        """
        self.image = None  # Variable image erstellen und ihr den Wert None (nichts zuweisen)
        if window is not None:  # Wenn window NICHT None ist, dann
            self.my_window = window  # Variable my_window = window
        else:  # sonst
            self.my_window = None  # Variable my_window = None

    """#############################################################
    # FUNCTION NAME: load_image                                    #
    # DESCRIPTION: loads an image and saves it as self.image       #
    # ARGUMENTS: image_name                                        #
    #                                                              #
    # ARGUMENT      TYPE    I/O     DESCRIPTION                    #
    # image_name    String          Name of the image to be loaded #
    #                                                              #
    # RETURNS:                                                     #
    #############################################################"""
    def load_image(self, image_name):
        self.image = cv.imread(image_name, cv.IMREAD_COLOR)
        # Lese ein Bild mit dem Namen image_name ein und speichert es als self.image

    """#############################################################
    # FUNCTION NAME: show_image                                     #
    # DESCRIPTION: shows an image in an Window                      #
    # ARGUMENTS: window(optional)                                   #
    #                                                               #
    # ARGUMENT  TYPE             DESCRIPTION                        #
    # window    WindowActions    Window the image will be drawed in #
    #                                                               #
    # RETURNS:                                                      #
    #############################################################"""
    def show_image(self, window=None):  # Optionaler Parameter window
        if window is None:  # Wenn window None ist
            window = self.my_window  # dann: window = self.my_window
        if self.image is not None:  # Wenn self.image NICHT None ist
            cv.imshow(window.windowName, self.image)  # dann zeige self.image im Fenster mit dem Namen window.windowName
        else:  # sonst
            print("No picture is loaded")  # Schreibe in die Konsole ...
        """
        # self.window.windowName Bedeutung:                                                                           #
        # self.window wird beim Erstellen einer Instanz vom Typ PictureActions auf den Parameter window gesetzt.      #
        # Der Parameter window ist von Typ WindowActions (also eine Instanz(Objekt)) diese Instanz hat ein Variable   #
        # self.windowName (siehe Klasse ImageActions).                                                                #
        # Mit self.window.windowName wird auf genau diese Variable zugegriffen.                                       #
        """

    """##############################################################
    # FUNCTION NAME: scale_image                                    #
    # DESCRIPTION: scales an image                                  #
    # ARGUMENTS: new_width, new_height                              #
    #                                                               #
    # ARGUMENT    TYPE   DESCRIPTION                                #
    # new_width   INT    new width of the Image                     #
    # new_height  INT    new height of the Image                    #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def scale_image(self, new_width, new_height):
        self.image = cv.resize(self.image, (new_width, new_height))  # Skaliere self.image auf new_width und new_height
        # und Speichere das Ergebnis in self.image

    """##############################################################
    # FUNCTION NAME: rotate_image                                   #
    # DESCRIPTION: rotates an image                                 #
    # ARGUMENTS: rotation_degrees                                   #
    #                                                               #
    # ARGUMENT          TYPE   DESCRIPTION                          #
    # rotation_degrees  INT    Rotation Value in Degrees (90,180 or 270) #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def rotate_image(self, rotation_degrees):
        rotate_code = None  # Variable rotate_code den Wert None zuweisen
        if 90 == rotation_degrees:  # Wenn rotation_degrees = 90
            rotate_code = cv.ROTATE_90_CLOCKWISE  # setze Variable rotate_code auf cv.ROTATE_90_CLOCKWISE
        elif 180 == rotation_degrees:  # wenn rotation_degrees = 180
            rotate_code = cv.ROTATE_180  # setze Variable rotate_code auf cv.ROTATE_180
        elif 270 == rotation_degrees:  # ...
            rotate_code = cv.ROTATE_90_COUNTERCLOCKWISE  # ...

        if rotate_code is not None:  # Wenn Variable rotation_code NICHT Null ist
            self.image = cv.rotate(self.image, rotate_code)  # Rotiere self.image um rotate_code und speichere das
            # Ergebnis als self.image
        else:  # sonst
            print("Enter 90, 180, or 270 as rotation_degrees")  # Schreibe in Konsole ...

    """##############################################################
     # FUNCTION NAME: flip_image                                     #
     # DESCRIPTION: flips an image                                   #
     # ARGUMENTS: flip_axis                                          #
     #                                                               #
     # ARGUMENT   TYPE      DESCRIPTION                              #
     # flip_axis  String    axis to flip at (value = X or Y or XY) #
     #                                                               #
     # RETURNS:                                                      #
     ##############################################################"""
    def flip_image(self, flip_axis):
        flip_code = None  # Variable flip_code den Wert None zuweisen

        if "X" == flip_axis:  # Wenn Parameter flip_axis = "X"
            flip_code = 0  # dann flip_code = 0
        elif "Y" == flip_axis:  # wenn Parameter flip_axis = "Y"
            flip_code = 1  # dann flip_code = 1
        elif "XY" == flip_axis:  # wenn...
            flip_code = -1  # dann...

        if flip_code is not None:  # Wenn Variable flip_code NICHT None ist
            self.image = cv.flip(self.image, flip_code)  # spiegle self.image mit flip_code und speichere das
            # Ergebnis als self.image
        else:  # sonst
            print("FlipAxis must be X or Y or XY")  # Schreibe in Konsole ...

    """##############################################################
     # FUNCTION NAME: add_blur_effect                                #
     # DESCRIPTION: blurs an image                                   #
     # ARGUMENTS: x, y                                               #
     #                                                               #
     # ARGUMENT   TYPE      DESCRIPTION                              #
     # x          INT       Blur-effect strength width               #
     # y          INT       Blur-effect strength height              #
     #                                                               #
     # RETURNS:                                                      #
     ##############################################################"""
    def add_blur_effect(self, x, y):
        self.image = cv.blur(self.image, (x, y))

    """##############################################################
    # FUNCTION NAME: spectrum_limit                                 #
    # DESCRIPTION: limits a color spectrum                          #
    # ARGUMENTS: lower_limit, upper_limit, is_colored               #
    #                                                               #
    # ARGUMENT     TYPE                      DESCRIPTION            #
    # lower_limit  TUPLE = (INT, INT , INT)  the lower_limit value: (h,s,v) #
    # upper_limit  TUPLE = (INT, INT , INT)  the upper_limit value: (h,s,v) #
    # is_colored   BOOLEAN                   defines if image is colored #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def spectrum_limit(self, lower_limit, upper_limit, is_colored):
        if is_colored:  # Wenn is_colored = True
            self.image = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)  # Farbraumkonvertierung vom bild self.image zu HSV
        self.image = cv.inRange(self.image, lower_limit, upper_limit)
        # Farbbereich zwischen lower_limit und upper_limit wird weiß, der Rest schwarz
        # das Ergebnis wird als self.image gespeichert

    """##############################################################
    # FUNCTION NAME: compare_images                                 #
    # DESCRIPTION: compares two images                              #
    # ARGUMENTS: second_image, compare_code(optional)               #
    #                                                               #
    # ARGUMENT      TYPE                  DESCRIPTION               #
    # second_image  PictureActions        an Object to compare      #
    # compare_code  INT(OpenCV constant)  How the images will be compared #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def compare_images(self, second_image, compare_code=None):
        if compare_code is None:
            comp_code = cv.CMP_NE
        else:
            comp_code = compare_code
        self.image = cv.compare(self.image, second_image.image, comp_code)

    @staticmethod
    def wait_key():
        cv.waitKey(0) & 0xFF


class WindowActions:
    def __init__(self):
        """
        Wird ausgeführt wenn eine Instanz (ein Objekt) der Klasse WindowActions erstellt wird
        """
        self.windowName = None

    """##############################################################
    # FUNCTION NAME: create_window                                  #
    # DESCRIPTION: creates a new window                             #
    # ARGUMENTS: name, width, height                                #
    #                                                               #
    # ARGUMENT   TYPE      DESCRIPTION                              #
    # name       String    Name of the winow                        #
    # width      INT       width of the window                      #
    # height     INT       height of the window                     #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def create_window(self, name, width, height):
        self.windowName = name              # Variable self.windowName is gleich dem Wert des Parameter name
        cv.namedWindow(self.windowName)     # erstelle ein Fenster mit dem Namen self.windowName
        cv.resizeWindow(self.windowName, width, height)
        # ändere die Größe des Fensters mit dem Namen self.name auf width, height

    """##############################################################
    # FUNCTION NAME: resize_window                                  #
    # DESCRIPTION: changes the size of an window                    #
    # ARGUMENTS: new_width, new_height                              #
    #                                                               #
    # ARGUMENT     TYPE      DESCRIPTION                            #
    # new_width    INT       new width of the window                #
    # new_height   INT       new height of the window               #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def resize_window(self, new_width, new_height):
        cv.resizeWindow(self.windowName, new_width, new_height)
        # ändere die Größe des Fensters mit dem Namen self.windowName auf new_width und new_height

    """##############################################################
    # FUNCTION NAME: move_window                                    #
    # DESCRIPTION: moves the window to a specific place             #
    # ARGUMENTS: pos_x, pos_y                                       #
    #                                                               #
    # ARGUMENT     TYPE      DESCRIPTION                            #
    # pos_x        INT       new X position (Pixel) of the window   #
    # pos_y        INT       new y position (Pixel) of the window   #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def move_window(self, pos_x, pos_y):
        cv.moveWindow(self.windowName, pos_x, pos_y)
        # verschiebe das Fenster mit dem Namen self.windowName auf die Position pos_x, pos_y

    """##############################################################
    # FUNCTION NAME: close_window                                   #
    # DESCRIPTION: closes a window                                  #
    # ARGUMENTS:                                                    #
    #                                                               #
    # ARGUMENT     TYPE      DESCRIPTION                            #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def close_window(self):
        cv.destroyWindow(self.windowName)


class ObjectActions:

    """##############################################################
    # FUNCTION NAME: __init__                                       #
    # DESCRIPTION: only on creating an instance of ObjectActions    #
    # ARGUMENTS: image                                              #
    #                                                               #
    # ARGUMENT    TYPE            DESCRIPTION                       #
    # image       ImageActions    the image the instance belongs to #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def __init__(self, image):
        """
        Wird ausgeführt wenn eine Instanz (ein Objekt) der Klasse ObjectActions erstellt wird
        """
        self.myImage = image
        # self.myImage wird auf den Wert des Parameters image gesetzt
        # der Parameter image ist ein Objekt vom Typ image
        self.fontFace = cv.FONT_HERSHEY_SIMPLEX
        # die Variable self.fontFace wird auf die Schriftart cv.FONT_HERSHEY_SIMPLEX gesetzt

    """##############################################################
    # FUNCTION NAME: get_color_code (static method = Class method)  #
    # DESCRIPTION: gets the color code (b,g,r) of an color          #
    # ARGUMENTS: color                                              #
    #                                                               #
    # ARGUMENT     TYPE      DESCRIPTION                            #
    # color        String    name of the color to get the code      #
    #                                                               #
    # RETURNS: color_code(Tuple)                                    #
    ##############################################################"""
    @staticmethod
    def get_color_code(color):
        if "red" == color:
            color_code = (0, 0, 255)
        elif "green" == color:
            color_code = (0, 255, 0)
        elif "blue" == color:
            color_code = (255, 0, 0)
        elif "white" == color:
            color_code = (255, 255, 255)
        else:
            color_code = (0, 0, 0)
        return color_code

    """##############################################################
    # FUNCTION NAME: draw_circle                                    #
    # DESCRIPTION: draws a circle                                   #
    # ARGUMENTS: center, radius, color_code, thickness(optional)    #
    #                                                               #
    # ARGUMENT     TYPE             DESCRIPTION                     #
    # center       Tuple(INT, INT)  center of the circle (in pixels relative to the image size) #
    # radius       INT              radius of the circle (in pixels) #
    # color_code   Tuple(INT,INT,INT) color of the circle (b, g, r) #
    # thickness    INT              thickness of the circle line    #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def draw_circle(self, center, radius, color_code, thickness=1):
        self.myImage.image = cv.circle(self.myImage.image, center, radius, color_code, thickness)

        """
        # self.myImage.image Bedeutung:                                                                           #
        # self.myImage wird beim Erstellen einer Instanz vom Typ Objekt Actions auf den Parameter image gesetzt.  #
        # Der Parameter image ist von Typ ImageActions (also eine Instanz(Objekt)) diese Instanz hat ein Variable #
        # self.image (siehe Klasse ImageActions).                                                                 #
        # Mit self.myImage.image wird auf genau diese Variable zugegriffen.                                       #
        """

    """###############################################################
    # FUNCTION NAME: draw_rectangle                                  #
    # DESCRIPTION: draw a rectangle                                  #
    # ARGUMENTS: start_point, end_point, color_code, thickness(optional) #
    #                                                                #
    # ARGUMENT     TYPE                DESCRIPTION                   #
    # start_point  Tuple(INT, INT)     upper left point of the rectangle (in pixels relative to the image)  #
    # end_point    Tuple(INT, INT)     lower right point of the rectangle (in pixels relative to the image) #
    # color_code   Tuple(INT,INT,INT)  color of the circle (b, g, r) #
    # thickness    INT              thickness of the circle line    #
    #                                                                #
    # RETURNS:                                                       #
    ###############################################################"""
    def draw_rectangle(self, start_point, end_point, color_code, thickness=1):
        self.myImage.image = cv.rectangle(self.myImage.image, start_point, end_point, color_code, thickness)

    """##############################################################
    # FUNCTION NAME: write_text                                     #
    # DESCRIPTION: writes a text                                    #
    # ARGUMENTS: text, x_pt, y_pt, font_scale, color_code, thickness(optional) #
    #                                                               #
    # ARGUMENT    TYPE            DESCRIPTION                       #
    # text        String          text to be written                #
    # x_pt        INT             left start position of the text   #
    # y_pt        INT             start height of the text          #
    # font_scale  INT             font size                         #
    # color_code  Tuple(INT,INT,INT) color of the circle (b, g, r)  #
    # thickness    INT              thickness of the circle line    #
    #                                                               #
    # RETURNS:                                                      #
    ##############################################################"""
    def write_text(self, text, x_pt, y_pt, font_scale, color_code, thickness=1):
        self.myImage.image = cv.putText(self.myImage.image, text, (x_pt, y_pt), self.fontFace, font_scale,
                                            color_code, thickness)


if __name__ == "__main__":

    """ Instanz(Objekt vom Typ WindowActions erstellen) """
    window1 = WindowActions()
    PictureActions.wait_key()
    """ Neues Fenter mit dem Name FensterNr_1 erstellen """
    window1.create_window("FensterNr_1", 100, 100)
    PictureActions.wait_key()
    """ Fenstergröße auf 400 X 400 Pixel ändern """
    window1.resize_window(400, 400)
    PictureActions.wait_key()
    """ Fenster Bewegen """
    window1.move_window(500, 5)
    PictureActions.wait_key()

    """ Instanz vom Typ PictureActions erstellen """
    picture1 = PictureActions(window1)

    """ Ein Bild (color.jpg) laden """
    picture1.load_image("color.jpg")

    """ Bild anzeigen lassen """
    picture1.show_image()
    PictureActions.wait_key()
    """ Bild drehen """
    picture1.rotate_image(90)
    picture1.show_image()
    PictureActions.wait_key()
    """ Bild spiegeln (An der X - Achse)"""
    picture1.flip_image("X")
    picture1.show_image()
    PictureActions.wait_key()

    """ Neue Instanz vom Typ ObjectActions erstellen """
    form = ObjectActions(picture1)

    """ (b,g,r) Farbcode für Weiß  """
    whiteColor = ObjectActions.get_color_code("white")

    """ Kreis einzeichnen """
    form.draw_circle((400, 400), 50, whiteColor, 5)
    picture1.show_image()
    PictureActions.wait_key()
    """ Rechteck einzeichnen """
    form.draw_rectangle((50, 50), (100, 100), whiteColor, 5)
    picture1.show_image()
    PictureActions.wait_key()
    """ Text einzeichnen """
    form.write_text("Test", 600, 450, 2, whiteColor, 3)
    picture1.show_image()
    PictureActions.wait_key()

    """ Bild kleiner Skalieren """
    picture1.scale_image(400, 400)
    picture1.show_image()
    PictureActions.wait_key()

    """ Fenster schließen """
    window1.close_window()

    """ Spektrum Filter und Compare """
    """ 1 Liste mit 4 Feldern erstellen """
    """ 1 Liste mit 3 Feldern erstellen """
    bilder = list(range(3))
    fenster = list(range(4))

    """Fenster erstellen"""
    fenster[0] = WindowActions()
    fenster[0].create_window("Bild1", 800, 800)

    """ Bild erstellen und color.jpg laden"""
    bilder[0] = PictureActions(fenster[0])
    bilder[0].load_image("color.jpg")
    bilder[0].show_image()
    PictureActions.wait_key()

    """ Werte des hellroten Kreises Links oben (h, s, v) : (0, 102, 255)"""
    """ das Spektrum auf den Kreis einschränken"""
    bilder[0].spectrum_limit((0, 0, 200), (20, 150, 255), True)
    bilder[0].show_image()
    PictureActions.wait_key()

    """ die schwarzen Punkte mithilfe des Weichzeichners (Blur) verschwinden lassen """
    bilder[0].add_blur_effect(20, 20)
    bilder[0].show_image()
    PictureActions.wait_key()

    """ Das Bild wieder Scharf machen, indem man mithilfe von spectrum_limit schwarze und weiße Bereiche trennt """
    bilder[0].spectrum_limit(150, 255, False)
    bilder[0].show_image()
    PictureActions.wait_key()

    """ Neues Fenster, Neues Bild erstellen, color.jpg laden und den Kreis rechts oben ausschneiden"""
    fenster[1] = WindowActions()
    fenster[1].create_window("Bild2", 800, 800)
    bilder[1] = PictureActions(fenster[1])
    bilder[1].load_image("color.jpg")
    bilder[1].show_image()
    PictureActions.wait_key()
    bilder[1].spectrum_limit((50, 100, 170), (130, 140, 190), True)
    bilder[1].show_image()
    PictureActions.wait_key()
    bilder[1].add_blur_effect(20, 20)
    bilder[1].show_image()
    PictureActions.wait_key()
    bilder[1].spectrum_limit(150, 255, False)
    bilder[1].show_image()
    PictureActions.wait_key()

    """ Neues Fenster, Neues Bild erstellen, color.jpg laden und den Kreis links unten ausschneiden"""
    fenster[2] = WindowActions()
    fenster[2].create_window("Bild3", 800, 800)
    bilder[2] = PictureActions(fenster[2])
    bilder[2].load_image("color.jpg")
    bilder[2].show_image()
    PictureActions.wait_key()
    bilder[2].spectrum_limit((0, 0, 0), (70, 255, 80), True)
    bilder[2].show_image()
    PictureActions.wait_key()
    bilder[2].add_blur_effect(20, 20)
    bilder[2].show_image()
    PictureActions.wait_key()
    bilder[2].spectrum_limit(150, 255, False)
    bilder[2].show_image()
    PictureActions.wait_key()

    """ bilder[0] bis bilder[2] zusammenfügen (compare) und in einem Neuen Fenster Anzeigen lassen """
    """ Neues Fenster erzeugen """
    fenster[3] = WindowActions()
    fenster[3].create_window("COMPARE", 800, 800)
    PictureActions.wait_key()

    """ bilder[0] und bilder[1] zusammenfügen """
    bilder[0].compare_images(bilder[1])
    bilder[0].show_image(fenster[3])
    PictureActions.wait_key()
    fenster[0].close_window()
    fenster[1].close_window()

    """ bilder[0] mit bilder[2] zusammenfügen """
    bilder[0].compare_images(bilder[2])
    PictureActions.wait_key()
    bilder[0].show_image(fenster[3])
    PictureActions.wait_key()
    fenster[2].close_window()
    PictureActions.wait_key()
    fenster[3].close_window()
