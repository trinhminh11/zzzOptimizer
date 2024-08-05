import React from "react";
import fireLogo from "../../assets/logo/agentsAttributes/Icon_Fire.jpg";
import electricLogo from "../../assets/logo/agentsAttributes/Icon_Electric.jpg";
import etherLogo from "../../assets/logo/agentsAttributes/Icon_Ether.jpg";
import iceLogo from "../../assets/logo/agentsAttributes/Icon_Ice.jpg";
import physicalLogo from "../../assets/logo/agentsAttributes/Icon_Physical.jpg";
import agentRinaLogo from "../../assets/logo/agents/Agent_Rina_Icon.jpg";
import sRankLogo from "../../assets/logo/agentsRanks/Icon_AgentRank_S.jpg";
import aRankLogo from "../../assets/logo/agentsRanks/Icon_AgentRank_A.jpg";
import anomalyRole from "../../assets/logo/agentsRoles/Icon_Anomaly.jpg";
import attackRole from "../../assets/logo/agentsRoles/Icon_Attack.jpg";
import supportRole from "../../assets/logo/agentsRoles/Icon_Support.jpg";
import victoriaFacton from "../../assets/logo/agentFactions/Victoria_Housekeeping_Icon.jpg";
import "./character.css";

function CharacterMainColumn() {
  return (
    <div className="character-right-column">
      <table>
        <thead>
          <tr>
            <th>Icon</th>
            <th>Name</th>
            <th>Rank</th>
            <th className="attibute">Attribute</th>
            <th className="fighting-style">Fighting Style</th>
            <th className="faction">Faction</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
            </td>
            <td>Alexandrina Sebastiane</td>
            <td>
              <img src={sRankLogo} alt="S Rank"></img>
            </td>
            <td>
              <img
                alt="Electric Logo"
                src={electricLogo}
                className="nav-icon"
              />
              <span>Electric</span>
            </td>
            <td>
              <img src={supportRole} alt="Support"></img>
              <span>Support</span>
            </td>
            <td>
              <img src={victoriaFacton} alt="Victoria"></img>
              <span>Victoria Housekeeping</span>
            </td>
          </tr>
          <tr>
            <td>
              <img alt="Rina Logo" src={agentRinaLogo} className="nav-icon" />
            </td>
            <td>Alexandrina Sebastiane</td>
            <td>
              <img src={sRankLogo} alt="S Rank"></img>
            </td>
            <td>
              <img
                alt="Electric Logo"
                src={electricLogo}
                className="nav-icon"
              />
              <span>Electric</span>
            </td>
            <td>
              <img src={supportRole} alt="Support"></img>
              <span>Support</span>
            </td>
            <td>
              <img src={victoriaFacton} alt="Victoria"></img>
              <span>Victoria Housekeeping</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default CharacterMainColumn;
