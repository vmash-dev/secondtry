from pywebio.input import input, slider
from pywebio.output import put_markdown, put_text, put_image

from classwork import pictures
import prices
from classwork.discount import DISCOUNT_TRIGGER_COST, DISCOUNT_PERCENTAGE

# Header
put_markdown("# 🍽️ Ресторан \"Смачна їжа\"")
put_markdown("---")

# MENU
put_markdown("## 📋 Menu:")

put_image(pictures.PICTURE_PIZZA)
put_text(f"🍕Pizza by {prices.PRICE_PIZZA} grn")

put_image(pictures.PICTURE_CAVIAR, width="300")
put_text(f"Caviar by {prices.PRICE_CAVIAR_10g} grn / 10g")

# Order placing
put_markdown("## Ordering:")

quantity_pizza = input("How many pizza do you like?", type="number", min=0, value=1)
quantity_caviar_g = slider(label="How much caviar do you like?", min_value=0, max_value=1000, value=10, step=10)
quantity_caviar = quantity_caviar_g / 10

# calculation
cost_pizza = quantity_pizza * prices.PRICE_PIZZA
cost_caviar = quantity_caviar * prices.PRICE_CAVIAR_10g
total_cost = cost_caviar + cost_pizza

discount_summa = 0
if total_cost >= DISCOUNT_TRIGGER_COST:
    discount_summa = round(total_cost * DISCOUNT_PERCENTAGE / 100, 0)

final_cost = total_cost - discount_summa

# ORDER
put_markdown("## RESULT:")

if cost_pizza:
    put_text(f"🍕Pizza: {quantity_pizza} / {prices.PRICE_PIZZA} grn = {cost_pizza}")
if cost_caviar:
    put_text(f"🍕cost_caviar: {quantity_caviar_g} / {prices.PRICE_CAVIAR_10g} grn/10g = {cost_caviar}")

if total_cost:
    put_text(f"Total cost: {total_cost}")


if discount_summa:
    put_text(f"discount_summa : {discount_summa}")
    put_text(f"))))))))))))))")


put_text(f"final_cost: {final_cost}")