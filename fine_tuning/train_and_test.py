from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

import run

__M_CODEBERT = 'codebert'
__M_PLBART = 'plbart'
__D_JAVA_PYTHON = 'java-python'
__D_PYTHON_JAVA = 'python-java'


def main():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-m', '--model',
                        choices=[__M_CODEBERT, __M_PLBART],
                        default='codebert',
                        help='Model to be used for fine tuning and testing.')
    parser.add_argument('-d', '--direction',
                        choices=[__D_JAVA_PYTHON, __D_PYTHON_JAVA],
                        default='java-python',
                        help='Direction of translation task; expected values: java-python or python-java.')
    parser.add_argument('-a', '--augmented',
                        action='store_true',
                        help='Use the dataset augmented with synthetically generated examples.')
    parser.add_argument('-l', '--load_path',
                        help='Specifies a model path to be used for testing, and skips training.')
    parser.add_argument('-b', '--batch_size_train',
                        type=int,
                        default='4',
                        help='Batch size to be used during training (reduce value if facing out of memory errors).')
    parser.add_argument('-s', '--step_count_train',
                        type=int,
                        default='50000',
                        help='Number of steps for which to train.')
    parser.add_argument('-e', '--example',
                        action='store_true',
                        help='Replace train/test data with a small example suitable for a dry run.')
    args = parser.parse_args()

    if args.model == __M_CODEBERT:
        pretrained_model = 'microsoft/codebert-base'
        model_type = 'roberta'
        config_and_token_name = 'roberta-base'
    elif args.model == __M_PLBART:
        pretrained_model = 'uclanlp/plbart-base'
        model_type = 'plbart'
        config_and_token_name = 'uclanlp/plbart-base'
    else:
        print('Wrong value for model.')
        return

    if args.direction == __D_JAVA_PYTHON:
        ext_a = 'java'
        ext_b = 'py'
    elif args.direction == __D_PYTHON_JAVA:
        ext_a = 'py'
        ext_b = 'java'
    else:
        print('Wrong value for direction.')
        return

    if args.example:
        train_n = test_n = 'example'
    else:
        train_n = 'train'
        test_n = 'test'

    file_prefix = 'augmented_' if args.augmented else ''
    output_dir = './out'

    if not args.load_path:
        run.main([
            '--do_train',
            '--model_type', model_type,
            '--model_name_or_path', pretrained_model,
            '--config_name', config_and_token_name,
            '--tokenizer_name', config_and_token_name,
            '--train_filename', f'../train_test_data/{file_prefix}{train_n}.{ext_a},../train_test_data/{file_prefix}{train_n}.{ext_b}',
            '--output_dir', output_dir,
            '--max_source_length', '512',
            '--max_target_length', '512',
            '--beam_size', '5',
            '--train_batch_size', str(args.batch_size_train),
            '--learning_rate', '0.00005',
            '--train_steps', str(args.step_count_train)
        ])

        args.load_path = f'{output_dir}/checkpoint-best-ppl/pytorch_model.bin'
        print()

    run.main(args_=[
        '--do_test',
        '--model_type', model_type,
        '--model_name_or_path', pretrained_model,
        '--config_name', config_and_token_name,
        '--tokenizer_name', config_and_token_name,
        '--load_model_path', args.load_path,
        '--dev_filename', f'../train_test_data/{test_n}.{ext_a},../train_test_data/{test_n}.{ext_b}',
        '--output_dir', output_dir,
        '--max_source_length', '512',
        '--max_target_length', '512',
        '--beam_size', '5',
        '--eval_batch_size', '16'
    ])


if __name__ == "__main__":
    main()
