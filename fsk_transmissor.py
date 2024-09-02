import numpy as np
import sounddevice as sd

# Configurações gerais
sample_rate = 48000  # Taxa de amostragem
duration = 0.1       # Duração de cada bit em segundos
freq_0 = 18000        # Frequência para representar bit 0 (Hz)
freq_1 = 20000        # Frequência para representar bit 1 (Hz)
header = '10101010'  # Padrão de sincronização (8 bits alternados)

# Função para gerar sinal para um bit específico
def generate_tone(bit):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    if bit == '1':
        return np.sin(2 * np.pi * freq_1 * t)
    else:
        return np.sin(2 * np.pi * freq_0 * t)

# Função para converter uma string em um sinal sonoro
def string_to_signal(data):
    signal = np.concatenate([generate_tone(bit) for byte in data for bit in format(ord(byte), '08b')])
    return signal

# Função para transmitir o sinal
def transmit(data):
    # Gera o sinal para o header e os dados
    header_signal = np.concatenate([generate_tone(bit) for bit in header])
    data_signal = string_to_signal(data)
    signal = np.concatenate((header_signal, data_signal))
    
    # Transmite o sinal
    sd.play(signal, samplerate=sample_rate)
    sd.wait()

# Exemplo de uso
if __name__ == "__main__":
    data_to_send = "Hello, friend!"
    transmit(data_to_send)
