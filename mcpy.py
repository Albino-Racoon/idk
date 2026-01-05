# LESSON 5 – COMBAT ARENA (vsa koda skupaj, popravljeno brez get_value)

# --- INVENTORY ---
def inventory():
    player.execute("/clear")
    mobs.give(mobs.target(NEAREST_PLAYER), DIAMOND_PICKAXE, 1)
    mobs.give(mobs.target(NEAREST_PLAYER), DIAMOND_SWORD, 1)
    mobs.give(mobs.target(NEAREST_PLAYER), DIAMOND_CHESTPLATE, 1)
    mobs.give(mobs.target(NEAREST_PLAYER), DIAMOND_HELMET, 1)
    mobs.give(mobs.target(NEAREST_PLAYER), DIAMOND_LEGGINGS, 1)
    mobs.give(mobs.target(NEAREST_PLAYER), DIAMOND_BOOTS, 1)
    mobs.give(mobs.target(NEAREST_PLAYER), BOW, 1)
    mobs.give(mobs.target(NEAREST_PLAYER), ARROW, 64)
    mobs.give(mobs.target(NEAREST_PLAYER), TRIDENT, 1)


# --- ROUND 1 ---
def round1(base, runda):
    # izpišemo številko runde poleg "ROUND"
    blocks.print(runda, SEA_LANTERN, positions.add(base, pos(5, 10, 45)), WEST)

    # spawn 1x vsaka pošast
    area1 = positions.add(base, pos(5, 5, 5))
    area2 = positions.add(base, pos(35, 5, 35))

    mobs.spawn(ZOMBIE, randpos(area1, area2))
    loops.pause(1000)
    mobs.spawn(SKELETON, randpos(area1, area2))
    loops.pause(1000)
    mobs.spawn(CREEPER, randpos(area1, area2))
    loops.pause(1000)
    mobs.spawn(BLAZE, randpos(area1, area2))
    loops.pause(1000)
    mobs.spawn(GHAST, randpos(area1, area2))

    # čas za čiščenje runde
    loops.pause(45000)


# --- ROUND 2 ---
def round2(base, runda):
    # power-upi
    mobs.apply_effect(SPEED, mobs.target(NEAREST_PLAYER), 20)
    mobs.apply_effect(REGENERATION, mobs.target(NEAREST_PLAYER), 20)
    mobs.apply_effect(STRENGTH, mobs.target(NEAREST_PLAYER), 20)

    # izpišemo številko runde poleg "ROUND"
    blocks.print(runda, SEA_LANTERN, positions.add(base, pos(5, 10, 45)), WEST)

    area1 = positions.add(base, pos(5, 5, 5))
    area2 = positions.add(base, pos(35, 5, 35))

    # spawn 2x vsaka pošast
    mobs.spawn(ZOMBIE, randpos(area1, area2))
    mobs.spawn(ZOMBIE, randpos(area1, area2))
    loops.pause(1000)

    mobs.spawn(SKELETON, randpos(area1, area2))
    mobs.spawn(SKELETON, randpos(area1, area2))
    loops.pause(1000)

    mobs.spawn(CREEPER, randpos(area1, area2))
    mobs.spawn(CREEPER, randpos(area1, area2))
    loops.pause(1000)

    mobs.spawn(BLAZE, randpos(area1, area2))
    mobs.spawn(BLAZE, randpos(area1, area2))
    loops.pause(1000)

    mobs.spawn(GHAST, randpos(area1, area2))
    mobs.spawn(GHAST, randpos(area1, area2))

    loops.pause(50000)

    # zmaga
    blocks.print("YOU WON", SEA_LANTERN, positions.add(base, pos(35, 20, 45)), WEST)


# --- PO SMRTI ---
def after_death():
    gameplay.set_game_mode(CREATIVE, mobs.target(NEAREST_PLAYER))

player.on_died(after_death)


# --- ARENA BUILDER (arena + gameplay) ---
def arenaBuilder():
    # setting the time to night
    gameplay.time_set(DayTime.NIGHT)

    # base pozicija (arena se zgradi malo stran od igralca)
    base = positions.add(player.position(), pos(10, 0, 0))

    # creating the arena (40x40, višina 5: y..y+4)
    blocks.fill(STONE_BRICKS, base, positions.add(base, pos(40, 4, 40)))

    # diamond bloki v kotih (platforma za beacon)
    blocks.fill(DIAMOND_BLOCK, positions.add(base, pos(0, 4, 0)), positions.add(base, pos(2, 4, 2)))
    blocks.fill(DIAMOND_BLOCK, positions.add(base, pos(38, 4, 0)), positions.add(base, pos(40, 4, 2)))
    blocks.fill(DIAMOND_BLOCK, positions.add(base, pos(0, 4, 38)), positions.add(base, pos(2, 4, 40)))
    blocks.fill(DIAMOND_BLOCK, positions.add(base, pos(38, 4, 38)), positions.add(base, pos(40, 4, 40)))

    # adding beacon blocks
    blocks.place(BEACON, positions.add(base, pos(1, 5, 1)))
    blocks.place(BEACON, positions.add(base, pos(39, 5, 1)))
    blocks.place(BEACON, positions.add(base, pos(1, 5, 39)))
    blocks.place(BEACON, positions.add(base, pos(39, 5, 39)))

    # creating stairs
    for i in range(15, 21):
        shapes.line(
            STONE_BRICK_STAIRS,
            positions.add(base, pos(-4, 0, i)),
            positions.add(base, pos(0, 4, i))
        )

    # inventory
    inventory()

    # ROUND text
    blocks.print("ROUND", SEA_LANTERN, positions.add(base, pos(35, 10, 45)), WEST)

    # survival mode
    gameplay.set_game_mode(SURVIVAL, mobs.target(NEAREST_PLAYER))

    # rounds
    round1(base, "1")
    round2(base, "2")


# --- CHAT COMMAND ---
player.on_chat("arena", arenaBuilder)
