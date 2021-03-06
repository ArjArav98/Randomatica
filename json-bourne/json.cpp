#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<utility>
using namespace std;

class JsonValidator {

	struct GraphNode {
		struct Neighbour {
			int id;
			vector< pair<char,char> > conditions;
		};

		int id;
		vector<Neighbour> neighbours;
	};

	vector<GraphNode> dfa;
	string word;
	int startNodeId, endNodeId;

	public:
	JsonValidator(string word) {
		dfa.push_back({
			.id=1,
			.neighbours = {
				{ .id=3,  .conditions = { make_pair('=','{') } },
				{ .id=1,  .conditions = { make_pair('=',' ') } },
				{ .id=13, .conditions = { make_pair('=','[') } },
				{ .id=2,  .conditions = { make_pair('^','.') } }
			}
		}); // Start node

		dfa.push_back({ .id=2, .neighbours = {} }); // Else node

		/* We start the DFA for the dictionary object.*/
		dfa.push_back({
			.id=3,
			.neighbours = {
				{ .id=4, .conditions = { make_pair('=','"') } },
				{ .id=3, .conditions = { make_pair('=',' ') } },
				{ .id=2, .conditions = { make_pair('^','.') } }
			}
		}); // Start brace.

		dfa.push_back({
			.id=4,
			.neighbours = {
				{ .id=6, .conditions = { make_pair('=','"')  } },
				{ .id=5, .conditions = { make_pair('^','^')  } }
			}
		}); // Key start quote.

		dfa.push_back({
			.id=5,
			.neighbours = {
				{ .id=6, .conditions = { make_pair('=','"') } }
			}
		}); // All string characters for key.

		dfa.push_back({
			.id=6,
			.neighbours = {
				{ .id=7, .conditions = { make_pair('=',':') } },
				{ .id=6, .conditions = { make_pair('=',' ') } },
				{ .id=2, .conditions = { make_pair('^','.') } }
			}
		}); // Key end quote.

		dfa.push_back({
			.id=7,
			.neighbours = {
				{ .id=8, .conditions = { make_pair('=','"') } },
				{ .id=7, .conditions = { make_pair('=',' ') } },
				{ .id=2, .conditions = { make_pair('^','.') } }
			}
		}); // Colon.

		dfa.push_back({
			.id=8,
			.neighbours = {
				{ .id=10, .conditions = { make_pair('=','"') } },	
				{ .id=9, .conditions = { make_pair('^','^') } }
			}
		}); // Value start quote.

		dfa.push_back({
			.id=9,
			.neighbours = {
				{ .id=10, .conditions = { make_pair('=','"') } }
			}
		}); // All string characters for value.

		dfa.push_back({
			.id=10,
			.neighbours = {
				{ .id=12, .conditions = { make_pair('=','}') } },
				{ .id=10, .conditions = { make_pair('=',' ') } },
				{ .id=11, .conditions = { make_pair('=',',') } },
				{ .id=2,  .conditions = { make_pair('^','.') } }
			}
		}); // Value end quote.

		dfa.push_back({
			.id=11,
			.neighbours = {
				{ .id=12, .conditions = { make_pair('=','}') } },
				{ .id=11, .conditions = { make_pair('=',' ') } },
				{ .id=4,  .conditions = { make_pair('=','"') } },
				{ .id=2,  .conditions = { make_pair('^','.') } }
			}
		}); // Comma.	

		dfa.push_back({
			.id=12,
			.neighbours = {
				{ .id=12, .conditions = { make_pair('=','}') } },
				{ .id=12, .conditions = { make_pair('=',' ') } }
			}
		}); // Closing brace.

		/* We continue the DFA for the array object. */
		dfa.push_back({
			.id=13,
			.neighbours = {
				{ .id=14, .conditions = { make_pair('=','"') } },
				{ .id=13, .conditions = { make_pair('=',' ') } },
				{ .id=2,  .conditions = { make_pair('^','.') } }
			}
		}); // Opening square bracket.

		dfa.push_back({
			.id=14,
			.neighbours = {
				{ .id=15, .conditions = { make_pair('=','"') } },
				{ .id=2,  .conditions = { make_pair('^','.') } }
			}
		}); // Opening array string quote.

		this->word = word;
		this->startNodeId = 1;
		this->endNodeId = 12;
	}

	int findNode(int nodeId) {
		for(int iter=0; iter<dfa.size(); iter++) 
			if(dfa[iter].id == nodeId) 
				return iter;

		return -1;
	}

	bool conditionsSatisfied(char character, vector< pair<char,char> > conditions) {
		for(int iter=0; iter<conditions.size(); iter++) {
			char cond_operator = conditions[iter].first;
			char cond_operand = conditions[iter].second;

			if(cond_operator == '=' && (character != cond_operand)) return false;
			else if(cond_operator == '>' && (character < cond_operand)) return false;
			else if(cond_operator == '<' && (character > cond_operand)) return false;
			else if(cond_operator == '^') continue;
		}

		return true;
	}

	int nextNode(int currentNodeId,char character) {
		//We need to iterate over all the neighbours of current node.
		int nodeIndex = findNode(currentNodeId);
		if(nodeIndex == -1) return -1;

		int noOfNeighbours = dfa[nodeIndex].neighbours.size();
		for(int iter=0; iter<noOfNeighbours; iter++) {
			if(conditionsSatisfied(character, dfa[nodeIndex].neighbours[iter].conditions))
				return dfa[nodeIndex].neighbours[iter].id;
		}

		return currentNodeId;
	}

	bool isValid() {
		int currentNodeId=startNodeId;

		for(int iter=0; iter<word.length(); iter++) {
			int nextNodeId = nextNode(currentNodeId, word[iter]);
			if(nextNodeId != -1) currentNodeId = nextNodeId;
			cout<<"Current node is "<<currentNodeId<<endl;
		}

		if(currentNodeId==endNodeId) return true;
		return false;
	}
};

int main() {
	JsonValidator json("{ \" \" : \" \", \"\":\"\"}  }");
	cout<<json.isValid()<<endl;
	return 0;
}
