import streamlit as st
import math

st.set_page_config(
    page_title="Tic-Tac-Toe AI",
    page_icon="🎮",
    layout="centered"
)

# ---------- Game Logic ----------

WINNING_COMBINATIONS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


def check_winner(board, player):
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] == player and board[b] == player and board[c] == player:
            return True
    return False


def is_draw(board):
    return all(cell != " " for cell in board)


def minimax(board, maximizing):
    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_draw(board):
        return 0

    if maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def get_ai_move(board):
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move


def reset_game():
    st.session_state.board = [" "] * 9
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.winner = None


# ---------- Initialize Game ----------

if "board" not in st.session_state:
    reset_game()


# ---------- UI ----------

st.title("🎮 Tic-Tac-Toe AI")
st.write("Play against an AI powered by the **Minimax algorithm**.")

st.info("You are ❌ X  |  Computer is ⭕ O")


# ---------- Display Board ----------

for row in range(3):
    cols = st.columns(3)

    for col in range(3):
        index = row * 3 + col

        with cols[col]:

            # Empty cell
            if st.session_state.board[index] == " ":

                if st.button(
                    " ",
                    key=f"cell_{index}",
                    use_container_width=True
                ):

                    # Player move
                    st.session_state.board[index] = "X"

                    # Check player win
                    if check_winner(st.session_state.board, "X"):
                        st.session_state.game_over = True
                        st.session_state.winner = "player"

                    # Check draw
                    elif is_draw(st.session_state.board):
                        st.session_state.game_over = True
                        st.session_state.winner = "draw"

                    else:
                        # AI move
                        ai_move = get_ai_move(st.session_state.board)

                        if ai_move is not None:
                            st.session_state.board[ai_move] = "O"

                        # Check AI win
                        if check_winner(st.session_state.board, "O"):
                            st.session_state.game_over = True
                            st.session_state.winner = "ai"

                        # Check draw
                        elif is_draw(st.session_state.board):
                            st.session_state.game_over = True
                            st.session_state.winner = "draw"

                    st.rerun()

            # X
            elif st.session_state.board[index] == "X":
                st.button(
                    "❌",
                    key=f"cell_{index}",
                    disabled=True,
                    use_container_width=True
                )

            # O
            else:
                st.button(
                    "⭕",
                    key=f"cell_{index}",
                    disabled=True,
                    use_container_width=True
                )


# ---------- Game Result ----------

if st.session_state.game_over:

    if st.session_state.winner == "player":
        st.success("🎉 You Win!")

    elif st.session_state.winner == "ai":
        st.error("🤖 Computer Wins!")

    else:
        st.warning("🤝 It's a Draw!")

else:
    st.write("### Your Turn")
    st.caption("Click an empty square to make your move.")


# ---------- Restart ----------

st.divider()

if st.button("🔄 New Game", use_container_width=True):
    reset_game()
    st.rerun()