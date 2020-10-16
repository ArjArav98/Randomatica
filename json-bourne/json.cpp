#include<iostream>
#include<vector>
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

	public:JsonValidator() {
		dfa.push_back(GraphNode());
		GraphNode node = {
			.id=1,
			.neighbours={
				{ .id=2, .conditions = { make_pair('=','a') } }
			}
		};
	}

};

int main() {
	JsonValidator json;
	return 0;
}
