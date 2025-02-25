import pm4py
from PBLES.event_log_dp_lstm import EventLogDpLstm


# Read Event Log Road_Traffic_Fine_Management_Process.xes
xes_file_path = "example_logs/Road_Traffic_Fine_Management_Process_short.xes"
event_log = pm4py.read_xes(xes_file_path)

# Initialize Model
bi_lstm_model = EventLogDpLstm(
    embedding_output_dims=128,
    epochs=5,
    batch_size=128,
    max_clusters=15,
    dropout=0.3,
    trace_quantile=0.9,
    l2_norm_clip=1.0,
    method="Bi-LSTM",
    units_per_layer=[32, 16]
)

# Train Model
bi_lstm_model.fit(event_log)
bi_lstm_model.save_model("models/Bi-LSTM_Road_Fines_u=32_e=inf")

