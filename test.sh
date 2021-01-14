if ! python3 scripts/warmup.py; then
	echo "ERROR: Some services failed to start successfully duing the warmup process"
	exit 1
fi
