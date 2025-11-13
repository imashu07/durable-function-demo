import azure.durable_functions as df

async def main(context: df.DurableOrchestrationContext):
    # fan-out / fan-in example: call HelloActivity for 3 cities in parallel
    tasks = []
    for city in ["Tokyo", "Seattle", "London"]:
        tasks.append(context.call_activity("HelloActivity", city))

    outputs = await context.task_all(tasks)
    return outputs

# register the orchestrator
main = df.Orchestrator.create(main)
