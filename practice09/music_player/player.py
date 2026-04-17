import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()
        self.music_folder = music_folder
        self.playlist = self.load_music()
        self.current_index = 0

        self.is_playing = False
        self.is_paused = False

        self.start_time = 0
        self.paused_time = 0

    def load_music(self):
        return [f for f in os.listdir(self.music_folder) if f.endswith((".mp3", ".wav"))]

    def play(self):
        if not self.playlist:
            print("No music files found.")
            return

        track = self.playlist[self.current_index]
        path = os.path.join(self.music_folder, track)

        # If paused → resume instead of restarting
        if self.is_paused:
            self.resume()
            return

        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0

        self.is_playing = True
        self.is_paused = False

        print(f"▶ Playing: {track}")

    def stop(self):
        # STOP = PAUSE
        if self.is_playing:
            pygame.mixer.music.pause()
            self.paused_time = pygame.time.get_ticks()

            self.is_playing = False
            self.is_paused = True

            print("⏸ Paused")

    def pause(self):
        self.stop()  # same behavior

    def resume(self):
        if self.is_paused:
            pygame.mixer.music.unpause()

            pause_duration = pygame.time.get_ticks() - self.paused_time
            self.start_time += pause_duration

            self.is_playing = True
            self.is_paused = False

            print("▶ Resumed")

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        if self.playlist:
            return self.playlist[self.current_index]
        return "No track"

    def get_position(self):
        if self.is_paused:
            return (self.paused_time - self.start_time) // 1000
        elif self.is_playing:
            return (pygame.time.get_ticks() - self.start_time) // 1000
        return 0

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)