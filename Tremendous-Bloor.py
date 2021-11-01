# Python code
#
userNum = 0
dealerNum = 0
dealerNum = randint(1, 11)
dealerNum += randint(1, 10)
userNum = randint(1, 11)
userNum += randint(1, 10)
basic.show_string("Hello & Welcome to: Sorta Blackjack!")
basic.show_string("Goal: try to beat the dealer by getting as close to 21 as possible without going over ")
basic.show_string("Press a to Hit press b to Stand")
basic.show_string("IMPORTANT: if the Dealers number is under 16 then they will Hit. If the dealers number is 17 or higher they will stand")
basic.show_string("Press A to hit or Press B to stand")
basic.show_string("Your Number is:")
basic.show_number(userNum)

def on_button_pressed_a():
  global userNum
  userNum += randint(1, 10)
  if userNum > 21:
    basic.show_icon(IconNames.Sad)
    basic.show_string("You Went Over! Your final number was:")
    basic.show_number(userNum)
  if userNum <= 21:
    basic.show_string("Your Number is now:")
    basic.show_number(userNum)
    basic.show_string("Press A to hit again")
    basic.show_string("Press B to stand")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
  global dealerNum
  basic.show_string("You Stood")
  if dealerNum <= 16:
    dealerNum += randint(1, 11)
    basic.clear_screen()
    basic.show_number(userNum)
  if dealerNum > 21:
    basic.show_string("The Dealer Went Over! You Win!")
    basic.show_string("There Number Was:")
    basic.show_number(dealerNum)
  if dealerNum == userNum:
    basic.show_string("Your Number was")
    basic.show_number(userNum)
    basic.show_string("The Dealers Number was")
    basic.show_number(dealerNum)
    basic.show_string("You Tied!")
    basic.clear_screen()
    basic.show_leds("""
      . . . . .
      . # . # .
      . . . . .
      # # # # #
      . . . . .
      """)
  if userNum > dealerNum:
    basic.show_string("Your Number was")
    basic.show_number(userNum)
    basic.show_string("The Dealers Number was")
    basic.show_number(dealerNum)
    basic.show_string("You Won!")
    basic.clear_screen()
    basic.show_leds("""
      . . . . .
      . # . # .
      . . . . .
      # . . . #
      . # # # .
      """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
  global dealerNum
  global userNum
  dealerNum = 0
  userNum = 0
  dealerNum = randint(1, 11)
  dealerNum += randint(1, 10)
  userNum = randint(1, 11)
  userNum += randint(1, 10)
  basic.show_string("Press A to hit or Press B to stand")
  basic.show_string("Your Number is:")
  basic.show_number(userNum)
input.on_gesture(Gesture.Shake, on_gesture_shake)
