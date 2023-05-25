//Solution

abstract class Adventure{
    constructor(protected name$: string){}

}
interface equiptToCollectGold{
    equipToCollectGold(): void
}
interface equiptToDefend{
    equiptToDefend(): void
}
interface equipToAttack{
    equiptToAttack(): void
}


class Ogre extends Adventure implemets equiptToCollectGold, equiptToDefend, equiptToAttack{
    fights(): void {
        console.log("fights with club and defends with shield")
    }
    equiptToCollectGold(): void{
        console.log("Can collect Gold")
    }
    equiptToDefend(): void{
        console.log("Can defend")
    }
    equiptToAttack(): void{
        console.log("Can attack")
    }
}


class Peons extends Adventure implemets equiptToCollectGold, equiptToDefend, equiptToAttack{
    fights(): void {
        console.log("fights with club and defends with shield")
    }
    equiptToCollectGold(): void{
        console.log("Can collect Gold")
    }
    equiptToDefend(): void{
        console.log("Can defend")
    }
    equiptToAttack(): void{
        console.log("Can attack")
    }
}


class Knight extends Adventure implemets equiptToCollectGold, equiptToDefend, equiptToAttack{
    fights(): void {
        console.log("fights with a Sword and defends with Armor")
    }
    equiptToCollectGold(): void{
        console.log("Can collect Gold")
    }
    equiptToDefend(): void{
        console.log("Can defend")
    }
    equiptToAttack(): void{
        console.log("Can attack")
    }
}


class Archer extends Adventure implemets equiptToCollectGold, equiptToDefend, equiptToAttack{
    fights(): void {
        console.log("fights with a Sword and defends with Armor")
    }
    equiptToCollectGold(): void{
        console.log("Can collect Gold")
    }
    equiptToDefend(): void{
        console.log("Can defend")
    }
    equiptToAttack(): void{
        console.log("Can attack")
    }
}


for (let class of allAdventure){

}
