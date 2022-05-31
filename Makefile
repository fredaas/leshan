all :
	@echo "Usage: make [options]"

run-demo-server :
	java -jar leshan-server-demo/target/leshan-server-demo-*-SNAPSHOT-jar-with-dependencies.jar

run-demo-client :
	java -jar leshan-client-demo/target/leshan-client-demo-*-SNAPSHOT-jar-with-dependencies.jar

run-demo-bootstrap-server :
	java -jar leshan-bsserver-demo/target/leshan-bsserver-demo-*-SNAPSHOT-jar-with-dependencies.jar
