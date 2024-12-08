
    result_df = import_title_data()
    result_df_body = import_body_data()
    model_title, label_encoder_title, top_subreddits_title_source, top_subreddits_title_target = make_title_model()
    model_body, label_encoder_body, top_subreddits_body_source, top_subreddits_body_target = make_body_model()
