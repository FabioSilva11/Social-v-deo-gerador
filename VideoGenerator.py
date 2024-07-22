from math import floor
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor as mp
import random, os
from gtts import gTTS

class VideoGenerator:
    def __init__(self, output_name_yt, output_name_tt):
        # Garante que há pelo menos um arquivo de som na lista
        sons = []
        for file in os.listdir("sons"):
            if file[-3:] == "mp3":
                sons.append("sons/" + file)
        if len(sons) == 0:
            raise Exception("Certifique-se de que há pelo menos um arquivo mp3 na pasta sons.")
        self.sons = sons

        # Garante que há pelo menos um clipe de vídeo na lista
        filmagens = []
        for file in os.listdir("filmagens"):
            if file[-3:] == "mp4":
                filmagens.append("filmagens/" + file)
        if len(filmagens) == 0:
            raise Exception("Certifique-se de que há pelo menos um arquivo mp4 na pasta filmagens.")
        self.filmagens = filmagens

        # Define os outros campos
        self.output_name_yt = output_name_yt
        self.output_name_tt = output_name_tt

    def get_audio_clip(self):
        som = random.choice(self.sons)
        clip = mp.AudioFileClip(som)
        return clip.set_duration(floor(clip.duration))

    def get_clip(self, clip_length):
        clip_name = "clip.mp4"
        filmagem = random.choice(self.filmagens)
        rand = random.randint(0, 813 - clip_length)
        ffmpeg_extract_subclip(filmagem, rand, rand + clip_length, targetname=clip_name)
        return clip_name    

    def generate_narration(self, text, language='pt'):
        tts = gTTS(text=text, lang=language)
        narration_file = "narration.mp3"
        tts.save(narration_file)
        narration_clip = mp.AudioFileClip(narration_file)
        return narration_clip

    def gen_meme_video(self, text, language='pt'):
        # Gera o áudio da narração
        narration = self.generate_narration(text, language)
        duration = narration.duration

        # Obtém o clipe de vídeo e define a narração como seu áudio
        clip_name = self.get_clip(duration)
        clip = mp.VideoFileClip(clip_name).set_audio(narration)

        # Divide o texto em palavras e calcula o tempo de exibição de cada uma
        words = text.split()
        num_words = len(words)
        word_duration = duration / num_words

        # Cria TextClips para cada palavra, cada um aparecendo em sequência
        text_clips = []
        for i, word in enumerate(words):
            txt_clip = mp.TextClip(word, fontsize=70, color='white', size=(1920, 1080))
            txt_clip = txt_clip.set_position('center').set_start(i * word_duration).set_duration(word_duration)
            text_clips.append(txt_clip)

        # Cria o vídeo final para YouTube com sobreposição de texto
        final_yt = mp.CompositeVideoClip([clip] + text_clips, size=(1920, 1024))
        final_yt.write_videofile(self.output_name_yt)

        # Ajusta o tamanho do vídeo e do texto para a resolução do TikTok (1080x1920)
        clip_tt = clip.resize(height=1920).crop(x_center=clip.w / 2, width=1080)
        text_clips_tt = [txt_clip.resize(height=1920).crop(x_center=txt_clip.w / 2, width=1080) for txt_clip in text_clips]

        # Cria o vídeo final para TikTok com sobreposição de texto
        final_tt = mp.CompositeVideoClip([clip_tt] + text_clips_tt, size=(1080, 1920))
        final_tt.write_videofile(self.output_name_tt)

        return self.output_name_yt, self.output_name_tt

# Exemplo de uso
output_name_yt = "youtube/meme_video_yt.mp4"
output_name_tt = "tiktok/meme_video_tt.mp4"
text = "Este é um exemplo de narração de meme"
video_gen = VideoGenerator(output_name_yt, output_name_tt)
video_gen.gen_meme_video(text, 'pt')
