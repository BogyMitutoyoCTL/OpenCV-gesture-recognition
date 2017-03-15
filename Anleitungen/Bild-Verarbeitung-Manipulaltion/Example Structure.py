# coding=utf-8
import """XXX"""


class ImageActions:
    def __init__(self):
        """ Code der beim Erstellen des Objekts ausgeführt wird """

    def load_image(self):
        """ Code um ein Bild einzulesen """

    def show_image(self):
        """ Code zum anzeigen eines Bildes """

    def scale_image(self):
        """ Code um die Größe des Bildes zu ändern """

    def rotate_image(self):
        """ Code um ein Bild zu rotieren """

    def flip_image(self):
        """ Code um ein Bild zu spiegeln """

    def add_blur_effect(self):
        """ Code für Weichzeichner """

    def spectrum_limit(self):
        """ Code um einen bestimmten Farbbereich zu extrahieren"""
        """ Das Ergebnis ist ein schwarz-weiß Bild"""

    def compare_images(self):
        """ Code um zwei Bilder zu einem zusammenzufügen"""


class WindowActions:
    def __init__(self):
        """ Code der beim Erstellen des Objekts ausgeführt wird """

    def create_window(self):
        """ Code um ein Fenster zu erstellen """

    def resize_window(self):
        """ Code um die Größe des Fensters zu ändern """

    def move_window(self):
        """ Code um das Fenster zu Bewegen """

    def close_window(self):
        """ Code um das Fenster zu schließen"""

    def wait_key(self):
        """ Code um zu warten bis eine Taste gedrückt wurde"""
        """ cv.waitKey(0) & 0xFF """


class ObjectActions:
    def __init__(self):
        """ Code der beim Erstellen des Objekts ausgeführt wird """

    def draw_circle(self):
        """ Code zum Zeichnen eines Kreises """

    def draw_rectangle(self):
        """ Code zum Zeichnen eines Rechtecks"""

    def write_text(self):
        """ Code um einen Text in ein Bild zu schreiben"""


if __name__ == "__main__":
    """
    Der hier stehende Programmcode wird beim Starten des Programms von oben nach unten ausgeführt
    Vergleichbar mit
        public static main(string[] args) - bei JAVA
    oder
        int main() - bei C
    """
    image = ImageActions()
    window = WindowActions()
    objects = ObjectActions()

    window.create_window()

    image.load_image()
    image.rotate_image()
    image.show_image()

    window.close_window()
