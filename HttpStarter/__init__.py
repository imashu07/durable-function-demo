import azure.functions as func
import azure.durable_functions as df

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    # start the orchestrator named "Orchestrator" (the folder name)
    instance_id = await client.start_new("Orchestrator", None, None)
    return client.create_check_status_response(req, instance_id)
