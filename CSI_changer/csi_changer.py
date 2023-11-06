import importlib
import numpy as np
import pandas as pd
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')
import config
decoder = importlib.import_module(f'decoders.{config.decoder}') # This is also an import

#stringからintへの変換可能な変数かを判定
def string_is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    #pcapファイル読み込み
    pcap_filename = input('Pcap File Name: ')
    bandwidth = input('Band Width: ')

    if '.pcap' not in pcap_filename:
        pcap_filepath = '/'.join([config.pcap_fileroot, pcap_filename+'.pcap'])

        #pcapファイル読み込みのデバック
        try:
            samples = decoder.read_pcap(pcap_filepath)
        except FileNotFoundError:
            print(f'File {pcap_filepath} not found.')
            exit(-1)

        command = input('> ')

        #複数のインデックス処理
        if ('-' in command) and string_is_int(command.split('-')[0]) and string_is_int(command.split('-')[1]):

            start = int(command.split('-')[0])
            end = int(command.split('-')[1])

            bandwidth = float(bandwidth) #帯域幅[MHz]
            nsub = int(bandwidth * 3.2) #subcarriarの総数を求める
            columns_amp = np.arange(-1 * nsub/2, nsub/2)
            columns_pha = np.arange(-1 * nsub/2, nsub/2)

            csi_amp_data = pd.DataFrame(columns=columns_amp)
            csi_pha_data = pd.DataFrame(columns=columns_pha)

            #インデックス分だけ繰り返す
            for index in tqdm(range(start, end+1)):

                csi = samples.get_csi(
                    index,
                    config.remove_null_subcarriers,
                    config.remove_pilot_subcarriers
                )

                value_amp = np.abs(csi)
                value_pha = np.angle(csi, deg=True)

                df_amp=pd.DataFrame(data=[value_amp], columns=columns_amp)
                df_pha=pd.DataFrame(data=[value_pha], columns=columns_pha)

                csi_amp_data = csi_amp_data.append(df_amp, ignore_index=True)
                csi_pha_data = csi_pha_data.append(df_pha, ignore_index=True)

            csi_amp_data.to_csv('./result/'+str(pcap_filename)+'_CSI_Amp.csv')
            csi_pha_data.to_csv('./result/'+str(pcap_filename)+'_CSI_Pha.csv')

            print("complete")

        else:
            print('Transform Error')
    else:
        print('Filename Error')