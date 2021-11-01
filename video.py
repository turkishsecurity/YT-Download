import os
from pytube import YouTube

print("-------------------------")
print("Yt Downloader By Xale")
print("xalesecurity.wordpress.com")
print("-------------------------")

url = input("İndirmek istediğiniz video : ")

yu = YouTube(url)

ys = yu.streams.get_highest_resolution()

print("Video indiriliyor.. ")

ys.download()

print("Video Bulunduğunuz Dizine İndirildi.")
print("Video Başlığı: ", ys.title)
