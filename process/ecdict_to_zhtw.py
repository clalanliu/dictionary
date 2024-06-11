import datasets
import opencc
converter = opencc.OpenCC('s2twp.json')


def translate_s2t(e):
    e['translation_t'] = converter.convert(e['translation'])
    e['translation'] = e['translation_t']
    e.pop('translation_t')
    return e


if __name__ == '__main__':
    ds = datasets.load_dataset('csv', data_files='data/ecdict.csv')['train'].filter(
        lambda e: e['translation'] is not None and len(e['translation']) > 0, num_proc=4)
    ds.map(
        translate_s2t, num_proc=4).to_csv('data/ecdict_tw.csv')
