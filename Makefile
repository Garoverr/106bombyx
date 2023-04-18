##
## EPITECH PROJECT, 2023
## 104intersection
## File description:
## makefile
##

NAME	=	106bombyx

SRC	=	106bombyx.py

$(NAME):
	cp $(SRC) $(NAME)
	chmod 755 $(NAME)

all:	$(NAME)
