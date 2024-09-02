import numpy as np
import sounddevice as sd
from scipy.fft import fft

# Configurações gerais
sample_rate = 48000  # Taxa de amostragem
duration = 0.1       # Duração de cada bit em segundos
freq_0 = 18000        # Frequência para representar bit 0 (Hz)
freq_1 = 20000        # Frequência para representar bit 1 (Hz)
tolerance = 80       # Tolerância para detecção de frequência (Hz)
header = '10101010'  # Padrão de sincronização (8 bits alternados)

# Função para detectar a frequência dominante em um sinal
def detect_frequency(signal):
    n = len(signal)
    freq = np.fft.fftfreq(n, d=1/sample_rate)
    fft_values = fft(signal)
    peak_freq = abs(freq[np.argmax(np.abs(fft_values))])
    return peak_freq

# Função para determinar se a frequência é 0 ou 1
def frequency_to_bit(frequency):
    if abs(frequency - freq_0) < tolerance:
        return '0'
    elif abs(frequency - freq_1) < tolerance:
        return '1'
    else:
        return None

# Função para verificar se o header está presente
def detect_header(signal):
    bits = []
    for i in range(0, len(signal), int(sample_rate * duration)):
        segment = signal[i:i + int(sample_rate * duration)]
        freq = detect_frequency(segment)
        bit = frequency_to_bit(freq)
        if bit is not None:
            bits.append(bit)
        if ''.join(bits[-8:]) == header:  # Checa se os últimos 8 bits correspondem ao header
            return True, signal[i + int(sample_rate * duration):]
    return False, None

# Função para converter o sinal capturado em uma string
def signal_to_string(signal):
    bits = []
    for i in range(0, len(signal), int(sample_rate * duration)):
        segment = signal[i:i + int(sample_rate * duration)]
        freq = detect_frequency(segment)
        bit = frequency_to_bit(freq)
        if bit is not None:
            bits.append(bit)
    byte_string = ''.join(bits)
    return ''.join([chr(int(byte_string[i:i + 8], 2)) for i in range(0, len(byte_string), 8)])

# Função para receber o sinal e decodificar
def receive():
    print("Aguardando sinal...")
    duration_seconds = 20  # Tempo máximo de escuta
    recording = sd.rec(int(duration_seconds * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    recording = np.squeeze(recording)
    
    # Detecta o início do sinal (header)
    header_found, remaining_signal = detect_header(recording)
    if header_found:
        message = signal_to_string(remaining_signal)
        print(f"Mensagem recebida: {message}")
    else:
        print("Header não detectado. Nenhuma mensagem recebida.")

# Exemplo de uso
if __name__ == "__main__":
    receive()