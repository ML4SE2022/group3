# shellcheck disable=SC1066
# shellcheck disable=SC2121

if [ "$1" = "plbart" ]; then
  pretrained_model="uclanlp/plbart-base"
  model_type="plbart"
  config_and_token_name="uclanlp/plbart-base"
else
  pretrained_model="microsoft/codebert-base"
  model_type="roberta"
  config_and_token_name="roberta-base"
fi

output_dir="./out/"
python3 run.py \
	--do_train \
	--do_eval \
	--model_type $model_type \
	--model_name_or_path $pretrained_model \
	--config_name $config_and_token_name \
	--tokenizer_name $config_and_token_name \
	--train_filename ./test_data/test/test.java,./test_data/test/test.py \
	--dev_filename ./test_data/val/val.java,./test_data/val/val.py \
	--output_dir $output_dir \
	--max_source_length 512 \
	--max_target_length 512 \
	--beam_size 5 \
	--train_batch_size 1 \
	--eval_batch_size 1 \
	--learning_rate 0.00005 \
	--train_steps 1 \
	--eval_steps 1