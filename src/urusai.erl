-module (urusai).

-export ([start/0, stop/0]).

start() ->
	application:ensure_all_started(urusai),
	urusai_http:start().

stop() -> application:stop(urusai).
