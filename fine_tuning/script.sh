# shellcheck disable=SC1066
# shellcheck disable=SC2121
pretrained_model="microsoft/codebert-base"
output_dir="./out/"
python3 run.py \
	--do_train \
	--do_eval \
	--model_type roberta \
	--model_name_or_path $pretrained_model \
	--config_name roberta-base \
	--tokenizer_name roberta-base \
	--train_filename ./train.java-python.java,./train.java-python.py \
	--dev_filename ./valid.java-python.java,./valid.java-python.py \
	--output_dir $output_dir \
	--max_source_length 512 \
	--max_target_length 512 \
	--beam_size 5 \
	--train_batch_size 1 \
	--eval_batch_size 1 \
	--learning_rate 0.00005 \
	--train_steps 5 \
	--eval_steps 5