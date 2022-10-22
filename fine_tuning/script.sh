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
	--model_type "plbart" \
	--model_name_or_path "uclanlp/plbart-base" \
	--config_name "uclanlp/plbart-base" \
	--tokenizer_name "uclanlp/plbart-base" \
	--train_filename ../data/test.java,../data/test.py \
	--dev_filename ./test_data/val/val.java,./test_data/val/val.py \
	--output_dir $output_dir \
	--max_source_length 512 \
	--max_target_length 512 \
	--beam_size 5 \
	--train_batch_size 8 \
	--eval_batch_size 5 \
	--learning_rate 0.00005 \
	--train_steps 1000 \
	--eval_steps 2

python3 run.py \
  --do_test \
	--model_type plbart \
	--model_name_or_path "uclanlp/plbart-base" \
	--config_name "uclanlp/plbart-base" \
	--tokenizer_name "uclanlp/plbart-base"  \
	--load_model_path $output_dir/checkpoint-best-bleu/pytorch_model.bin \
	--dev_filename ../data/val.java,../data/val.py \
	--output_dir $output_dir \
	--max_source_length 512 \
	--max_target_length 512 \
	--beam_size 5 \
	--eval_batch_size 16