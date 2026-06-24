You are working in `/app`.

There is a small Apache-style access log at `/app/access.log`. Read it and create `/app/report.json`.

The JSON must contain these three fields and no others:

- `total_requests`: number of non-blank log lines.
- `unique_ips`: number of different client IPs. The client IP is the first value on each log line.
- `top_path`: the request path that appears most often inside the quoted HTTP request, for example `/index.html` from `"GET /index.html HTTP/1.1"`. If there is a tie, choose the path that comes first alphabetically.

Only write the JSON file. Do not make a separate text report or add extra fields.

You have 120 seconds to complete the task.
