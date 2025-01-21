from recbole.quick_start import run_recbole

if __name__ == '__main__':
    # 参数配置文件路径
    config_file_path = 'configs/lightgcn_config.yaml'
    # 选择模型算法和数据集
    run_recbole(model='LightGCN', dataset='hmx-400k', config_file_list=[config_file_path])
