


class ErrorHandler:
    def error_handling(self, pic_coordonates:str):
        if (pic_coordonates == None) or (pic_coordonates == ""):
            print(f"Couldn't find image coordonates")
            return None