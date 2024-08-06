import AgentInfo from "./AgentInfo";

class Agent {}

export default function agentProcessing() {
  let agents = [];

  return (
    <div>
      <AgentInfo agents={agents} />
    </div>
  );
}
