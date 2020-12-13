#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <vector>
#include <regex>
#include <boost/algorithm/string.hpp>

#include <algorithm>

using namespace std;
using namespace boost;

class DirectedGraph {
    map<string, vector<string>> adjacencyListsP1;
    map<string, vector<pair<string, int>>> adjacencyListsP2;
    void DFSUtil(int v, bool visited[]);

  public:
    void addEdge(string fromBag, string toBag);
    void addQuantifiedEdge(string fromBag, string toBag, int totagQuantity);
    void print();
    int numberBagsContaining(string innerBag);
    set<string> bagsContaining(string innerBag);
    int numberBagsContainedBy(string outerBag);
};

void DirectedGraph::addEdge(string fromBag, string toBag) {
  if (adjacencyListsP1.find(fromBag) != adjacencyListsP1.end()) {
    adjacencyListsP1[fromBag].push_back(toBag);
  } else {
    vector<string> toBagList{ toBag };
    adjacencyListsP1.insert(make_pair(fromBag, toBagList));
  }
}

void DirectedGraph::addQuantifiedEdge(string fromBag, string toBag, int toBagQuantity) {
  pair<string, int> toBagPair = make_pair(toBag, toBagQuantity);
  if (adjacencyListsP2.find(fromBag) != adjacencyListsP2.end()) {
    adjacencyListsP2[fromBag].push_back(toBagPair);
  } else {
    vector<pair<string, int>> toBagList{ toBagPair };
    adjacencyListsP2.insert(make_pair(fromBag, toBagList));
  }
}


int DirectedGraph::numberBagsContaining(string innerBag) {
  set<string> bagsContainingInnerBag = this->bagsContaining(innerBag);
  return bagsContainingInnerBag.size();
}

set<string> DirectedGraph::bagsContaining(string innerBag) {
  vector<string> outerBags = adjacencyListsP1[innerBag];
  set<string> bagsContainingInnerBag;
  for (string outerBag: outerBags) {
    bagsContainingInnerBag.insert(outerBag);
    set<string> bagsContainingOuterBag = this->bagsContaining(outerBag);
    bagsContainingInnerBag.insert(bagsContainingOuterBag.cbegin(), bagsContainingOuterBag.cend());
  }
  return bagsContainingInnerBag;
}

int DirectedGraph::numberBagsContainedBy(string outerBag) {
  int numberBagsContained = 0;
  vector<pair<string, int>> bagsContained = adjacencyListsP2[outerBag];
  for (pair<string, int> bagContained: bagsContained) {
    numberBagsContained = numberBagsContained + bagContained.second + bagContained.second * this->numberBagsContainedBy(bagContained.first);
  }
  return numberBagsContained;
}

void DirectedGraph::print() {
  for (auto const& x : adjacencyListsP2) {
    cout << x.first << " contains " ;
    for (pair<string, int> y: x.second) {
      cout << y.second << " " << y.first << " bags, ";
    }
    cout << endl;
  }
}

vector<string> readInputFile(string inputFile) {
  vector<string> returnValues = {};
  string lineRead;
  ifstream fileStream;
  fileStream.open (inputFile);
  while (getline (fileStream, lineRead)) {
    returnValues.push_back(lineRead);
  }
  fileStream.close();
  return returnValues;
}


string extractOuterBagType(string inputString) {
  regex bagRegex("[A-Za-z][ a-zA-Z]+?[a-zA-Z](?= bags contain)");
  smatch bagMatch;
  regex_search(inputString, bagMatch, bagRegex);
  return bagMatch[0];
}

vector<string> extractInnerBagType(string inputString) {
  regex bagRegex("[A-Za-z][ a-zA-Z]+?[a-zA-Z](?= bag)");
  smatch bagMatch;
  vector<string> returnValues;
  regex_search(inputString, bagMatch, bagRegex);
  inputString = bagMatch.suffix();
  while (regex_search(inputString, bagMatch, bagRegex)) {
    if (bagMatch[0] != "bags contain no other") {
      returnValues.push_back(bagMatch[0]);
    }
    inputString = bagMatch.suffix();
  }

  return returnValues;
}

vector<int> extractInnerBagQuantities(string inputString) {
  regex quantityRegex("\\d+");
  smatch quantityMatch;
  vector<int> returnValues;
  while (regex_search(inputString, quantityMatch, quantityRegex)) {
    returnValues.push_back(stoi(quantityMatch[0]));
    inputString = quantityMatch.suffix();
  }

  return returnValues;
}


int main( int argc, char* argv[] ) {
  string input_file= argv[1];
  string part = argv[2];

  vector<string> inputLines = readInputFile("input.txt");

  DirectedGraph bagGraph = DirectedGraph();

  if (part == "1") {
    for (string inputLine: inputLines) {
      string outerBagType = extractOuterBagType(inputLine);
      vector<string> innerBagTypes = extractInnerBagType(inputLine);
      for (string innerBagType: innerBagTypes) {
          bagGraph.addEdge(innerBagType, outerBagType);
      }
    }
    cout << bagGraph.numberBagsContaining("shiny gold") << endl;

  } else if (part == "2") {
    string outerBagType;
    vector<string> innerBagTypes;
    vector<int> innerBagQuantities;
    string innerBagType;
    int innerBagQuantity;

    for (string inputLine: inputLines) {

      outerBagType = extractOuterBagType(inputLine);
      innerBagTypes = extractInnerBagType(inputLine);
      innerBagQuantities = extractInnerBagQuantities(inputLine);

      for (int i=0; i<innerBagTypes.size(); i++) {
        innerBagType = innerBagTypes[i];
        innerBagQuantity = innerBagQuantities[i];
        bagGraph.addQuantifiedEdge(outerBagType, innerBagType, innerBagQuantity);
      }
    }
    cout << bagGraph.numberBagsContainedBy("shiny gold");


  } else {
    cout << "Part requested not recognised" << endl;
  }

  return 0;
}
