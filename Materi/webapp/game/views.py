from django.shortcuts import render
from django.http import HttpResponse

# def index_view(request):
#     return HttpResponse("<h1>Hello World!</h1>")

# def index(request):
#     # html_content = "<h1>Portal Game!</h1>"
#     html_content = """
#     <!DOCTYPE html>
#     <html lang="id">
#     <head>
#         <meta charset="UTF-8">
#         <title>Nexus Game Portal - Lobi Utama</title>
#         <style>
#             body {
#                 background-color: #222222;
#                 color: #ffffff;
#                 font-family: Arial, sans-serif;
#                 padding: 30px;
#             }
#             a {
#                 color: #4CAF50;
#                 text-decoration: none;
#             }
#             a:hover {
#                 text-decoration: underline;
#             }
#         </style>
#     </head>
#     <body>
#         <h1>🕹️ Nexus Game Hub 🕹️</h1>
#         <hr>
#         <p>Selamat datang di lobi utama! Silakan pilih menu di bawah ini untuk menguji Routing URL Anda:</p>
        
#         <ul>
#             <li>
#                 <h2><a href="/game/moba/">⚔️ Mobile Legends</a></h2>
#                 <p>Pilih role hero terbaikmu dan pelajari tugasnya di Land of Dawn.</p>
#             </li>
#             <br>
#             <li>
#                 <h2><a href="/game/genshin/">✨ Genshin Impact</a></h2>
#                 <p>Eksplorasi 7 elemen Teyvat dan pelajari reaksi elemental-nya.</p>
#             </li>
#         </ul>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_content)

def index(request):
    # kirim data ke template html
    context = {
        "portal_name": "Portal Anak Warnet"
    }

    return render(request, 'portal.html', context)

def moba_view(request):
    return render(request, 'moba.html')

def genshin_view(request):
    return render(request, 'genshin.html')

def dota_view(request):
    return render(request, 'dota.html')