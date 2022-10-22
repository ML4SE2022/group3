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
	--model_type $model_type \
	--model_name_or_path $pretrained_model \
	--config_name $config_and_token_name \
	--tokenizer_name $config_and_token_name \
	--train_filename ../train.java,../train.py \
	--output_dir $output_dir \
	--max_source_length 512 \
	--max_target_length 512 \
	--beam_size 5 \
	--train_batch_size 4 \
	--learning_rate 0.00005 \
	--train_steps 1000 \

python3 run.py \
  --do_test \
	--model_type $model_type \
	--model_name_or_path $pretrained_model \
	--config_name $config_and_token_name \
	--tokenizer_name $config_and_token_name  \
	--load_model_path $output_dir/checkpoint-best-bleu/pytorch_model.bin \
	--dev_filename ../test.java,../test.py \
	--output_dir $output_dir \
	--max_source_length 512 \
	--max_target_length 512 \
	--beam_size 5 \
	--eval_batch_size 16