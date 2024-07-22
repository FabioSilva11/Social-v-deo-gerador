# Social-video-gerador

### Documentação do VideoGenerator

#### Sumário
- [Introdução](#introdução)
- [Instalação](#instalação)
- [Estrutura do Código](#estrutura-do-código)
- [Uso](#uso)
- [Exemplo de Uso](#exemplo-de-uso)
- [Métodos](#métodos)

---

### Introdução

A classe `VideoGenerator` é projetada para criar vídeos de meme com narração de texto. O código permite gerar dois tipos de vídeos com resoluções específicas para YouTube (1920x1024) e TikTok (1080x1920), e salva os vídeos em pastas diferentes.

### Instalação

Para utilizar essa classe, é necessário ter as seguintes bibliotecas Python instaladas:

```sh
pip install moviepy gtts
```

### Estrutura do Código

O código está organizado em uma classe chamada `VideoGenerator`, que possui os seguintes métodos principais:

- `__init__(self, output_name_yt, output_name_tt)`: Construtor da classe.
- `get_audio_clip(self)`: Obtém um clipe de áudio aleatório da pasta `sounds`.
- `get_clip(self, clip_length)`: Obtém um clipe de vídeo aleatório da pasta `footage` com a duração especificada.
- `generate_narration(self, text, language='pt')`: Gera a narração do texto usando `gTTS`.
- `gen_meme_video(self, text, language='pt')`: Gera o vídeo final com a narração do texto e salva as versões para YouTube e TikTok.

### Uso

Para utilizar a classe `VideoGenerator`, siga as etapas abaixo:

1. **Crie as pastas necessárias**: Crie as pastas `sounds` e `footage` no mesmo diretório onde o código será executado.
2. **Adicione arquivos de mídia**:
   - Adicione arquivos `.mp3` na pasta `sounds`.
   - Adicione arquivos `.mp4` na pasta `footage`.
3. **Inicialize a classe e gere o vídeo**: Passe os nomes dos arquivos de saída e o texto de narração para a classe.

### Exemplo de Uso

```python
from video_generator import VideoGenerator

# Nomes dos arquivos de saída para YouTube e TikTok
output_name_yt = "youtube/meme_video_yt.mp4"
output_name_tt = "tiktok/meme_video_tt.mp4"

# Texto a ser narrado no vídeo
text = "Este é um exemplo de narração de meme"

# Inicialize a classe
video_gen = VideoGenerator(output_name_yt, output_name_tt)

# Gere o vídeo
video_gen.gen_meme_video(text, 'pt')
```

### Métodos

#### `__init__(self, output_name_yt, output_name_tt)`
Construtor da classe. Inicializa as listas de sons e vídeos a partir das pastas `sounds` e `footage`. Define os nomes dos arquivos de saída para YouTube e TikTok.

- **Parâmetros**:
  - `output_name_yt`: Nome do arquivo de saída para o vídeo do YouTube.
  - `output_name_tt`: Nome do arquivo de saída para o vídeo do TikTok.

#### `get_audio_clip(self)`
Obtém um clipe de áudio aleatório da pasta `sounds`.

- **Retorno**: `AudioFileClip` com a duração ajustada.

#### `get_clip(self, clip_length)`
Obtém um clipe de vídeo aleatório da pasta `footage` com a duração especificada.

- **Parâmetros**:
  - `clip_length`: Duração do clipe em segundos.

- **Retorno**: Nome do arquivo do clipe de vídeo gerado.

#### `generate_narration(self, text, language='pt')`
Gera a narração do texto usando `gTTS` e salva o arquivo de áudio.

- **Parâmetros**:
  - `text`: Texto a ser narrado.
  - `language`: Idioma da narração (padrão é 'pt' para português).

- **Retorno**: `AudioFileClip` do arquivo de áudio gerado.

#### `gen_meme_video(self, text, language='pt')`
Gera o vídeo final com a narração do texto e salva as versões para YouTube e TikTok.

- **Parâmetros**:
  - `text`: Texto a ser narrado no vídeo.
  - `language`: Idioma da narração (padrão é 'pt' para português).

- **Retorno**: Nomes dos arquivos de saída para YouTube e TikTok.

---

Essa documentação fornece uma visão geral de como usar a classe `VideoGenerator` para gerar vídeos de meme com narração de texto, e descreve cada método disponível na classe.
