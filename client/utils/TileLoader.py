"""
MIT License

Copyright (c) 2022 Voltage Software

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import pygame
from image.Image import Image

class TileLoader:

    def __init__(self, main):
        self.main = main

    def loadTiles(self):
        y = 0
        for line in self.main.game_map["tiles"]:
            x = 0
            for each in line:
                if each == "1":
                    image = Image("zemin/zemin.png", (x * 32, y * 32))
                    rect = pygame.Rect(x * 32, y * 32, 32, 32)
                if each == "2":
                    image = Image("duvar/duvar.png", (x * 32, y * 32))
                    rect =  pygame.Rect(x * 32, y * 32, 32, 32)
                if each == "3":
                    image = Image("duvar/sadecesagvar.png", (x * 32, y * 32))
                    rect =  pygame.Rect(x * 32, y * 32, 32, 32)
                if each == "4":
                    image = Image("duvar/sadecesolvar.png", (x * 32, y * 32))
                    rect =  pygame.Rect(x * 32, y * 32, 32, 32)
                if each == "5":
                    image = Image("duvar/sagveustyok.png", (x * 32, y * 32))
                    rect =  pygame.Rect(x * 32, y * 32, 32, 32)
                if each == "6":
                    image = Image("duvar/solveustyok.png", (x * 32, y * 32))
                    rect =  pygame.Rect(x * 32, y * 32, 32, 32)
                if each != "#" and each != "0":
                    self.main.tile_rects.append(rect)
                    if self.main.checkCollide(self.main.character.rect, rect):
                        self.main.gravity_y = -0.2
                    self.main.window.blit(image.img, rect)
                x += 1
            y += 1
