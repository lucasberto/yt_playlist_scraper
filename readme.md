### Sobre

Esse script tem como objetivo extrair o link de todos os vídeos de uma ou mais playlists do youtube.

### Como usar

1. Instale o python 3.8 ou superior
2. Instale a biblioteca YoutubeDL: `pip install youtube-dl`
3. Coloque os links das playlists (um por linha) no arquivo `playlists.txt` (use o link da playlist, e não o link de um vídeo específico da playlist, exemplo válido: https://www.youtube.com/playlist?list=PLidIjcybOMhznm5SOjGCt5wBIJMsPvr8P)
4. Execute o script: `python scraper.py`
5. O script irá criar um arquivo CSV (compatível com Excel) para cada playlist cotendo os títulos e links dos vídeos dentro da pasta `playlist_output`

Para mais informações sobre a bibilioteca YoutubeDL, acesse: https://github.com/ytdl-org/youtube-dl
