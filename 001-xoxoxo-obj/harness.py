from game import Game
from input_con import InputCon
from output_con import OutputCon


class Harness():
  def __init__(self, output, inputs):
    self._game = Game()
    self._output = output
    self._inputs = inputs

  def Start(self):
    self._output.show_welcome()

    while True:
      self._output.show_board(self._game.get_board())

      player_id = self._game.get_turn_no()
      player = self._game.get_turn()

      self._output.show_player_turn(player)

      while True:
        move = self._inputs[player_id].get_move()
        if move is None:
          self._output.show_move_error(player)
          continue 

        if self._game.make_move(move) is False:
          self._output.show_move_error(player)
          continue

        break

      if not self._game.get_end():
        continue

      # End of game.
      self._output.show_board(self._game.get_board())
      w = self._game.get_winner()
      if w is None:
        # Draw.
        self._output.show_draw()
      else:
        self._output.show_winner(w)
      break

def main():
  inputcon1 = InputCon()
  inputcon2 = InputCon()
  outputcon = OutputCon()
      
  player_inputs = [ inputcon1, inputcon2 ]
  player_output = outputcon

  h = Harness(player_output, player_inputs)
  h.Start()


if __name__ == "__main__":
  main()


