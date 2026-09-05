# Concept
gruops of viruses slide and combat in a controlled enviroment

# Viruses
stats:
{
    life: int,
    strenght: int,
    group: Group
}
Every tick:
- decide which direction to slide (50% chance of going in the same direction, 50% chance of going in a random direction)
- bounce when collide to a wall
- hurt and get hurt when collide to other virus if it's not from it's group
- get stronger if it kills someone
- heal if it's hurt

# Random
Cada bactéria recebe inicialmente 10 pontos para ser distribuído aleatóriamente entre vida e força (vida -> pega uma fatia aleatória (máx 90%), força -> resto)