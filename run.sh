# Run evaluation script
python astronet/evaluate.py \
--model=AstroCNNModel \
--config_name=local_global \
--eval_files=tfrecords/test* \
--model_dir=models_final/model_dc_se/model_1