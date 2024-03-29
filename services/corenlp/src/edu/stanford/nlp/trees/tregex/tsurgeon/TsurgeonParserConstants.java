/* Generated By:JJTree&JavaCC: Do not edit this line. TsurgeonParserConstants.java */
package edu.stanford.nlp.trees.tregex.tsurgeon;


/**
 * Token literal values and constants.
 * Generated by org.javacc.parser.OtherFilesGen#start()
 */
interface TsurgeonParserConstants {

  /** End of File. */
  int EOF = 0;
  /** RegularExpression Id. */
  int OPEN_BRACKET = 5;
  /** RegularExpression Id. */
  int IF = 6;
  /** RegularExpression Id. */
  int NOT = 7;
  /** RegularExpression Id. */
  int EXISTS = 8;
  /** RegularExpression Id. */
  int DELETE = 9;
  /** RegularExpression Id. */
  int PRUNE = 10;
  /** RegularExpression Id. */
  int RELABEL = 11;
  /** RegularExpression Id. */
  int EXCISE = 12;
  /** RegularExpression Id. */
  int INSERT = 13;
  /** RegularExpression Id. */
  int MOVE = 14;
  /** RegularExpression Id. */
  int REPLACE = 15;
  /** RegularExpression Id. */
  int CREATE_SUBTREE = 16;
  /** RegularExpression Id. */
  int ADJOIN = 17;
  /** RegularExpression Id. */
  int ADJOIN_TO_HEAD = 18;
  /** RegularExpression Id. */
  int ADJOIN_TO_FOOT = 19;
  /** RegularExpression Id. */
  int COINDEX = 20;
  /** RegularExpression Id. */
  int NAME = 21;
  /** RegularExpression Id. */
  int CLOSE_BRACKET = 22;
  /** RegularExpression Id. */
  int SELECTION = 23;
  /** RegularExpression Id. */
  int GENERAL_RELABEL = 24;
  /** RegularExpression Id. */
  int IDENTIFIER = 25;
  /** RegularExpression Id. */
  int LOCATION_RELATION = 26;
  /** RegularExpression Id. */
  int REGEX = 27;
  /** RegularExpression Id. */
  int QUOTEX = 28;
  /** RegularExpression Id. */
  int HASH_INTEGER = 29;
  /** RegularExpression Id. */
  int TREE_NODE_TERMINAL_LABEL = 30;
  /** RegularExpression Id. */
  int TREE_NODE_NONTERMINAL_LABEL = 31;
  /** RegularExpression Id. */
  int CLOSE_PAREN = 32;

  /** Lexical state. */
  int OPERATION = 0;
  /** Lexical state. */
  int CONDITIONAL = 1;
  /** Lexical state. */
  int DEFAULT = 2;

  /** Literal token values. */
  String[] tokenImage = {
    "<EOF>",
    "\" \"",
    "\"\\r\"",
    "\"\\t\"",
    "\"\\n\"",
    "\"[\"",
    "\"if\"",
    "\"not\"",
    "\"exists\"",
    "\"delete\"",
    "\"prune\"",
    "\"relabel\"",
    "\"excise\"",
    "\"insert\"",
    "\"move\"",
    "\"replace\"",
    "\"createSubtree\"",
    "\"adjoin\"",
    "\"adjoinH\"",
    "\"adjoinF\"",
    "\"coindex\"",
    "<NAME>",
    "\"]\"",
    "<SELECTION>",
    "<GENERAL_RELABEL>",
    "<IDENTIFIER>",
    "<LOCATION_RELATION>",
    "<REGEX>",
    "<QUOTEX>",
    "<HASH_INTEGER>",
    "<TREE_NODE_TERMINAL_LABEL>",
    "<TREE_NODE_NONTERMINAL_LABEL>",
    "\")\"",
  };

}
