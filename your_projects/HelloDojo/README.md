<picture>
  <source media="(prefers-color-scheme: dark)" srcset=".github/mark-dark.svg">
  <img alt="Dojo logo" align="right" width="120" src=".github/mark-light.svg">
</picture>

<a href="https://twitter.com/dojostarknet">
<img src="https://img.shields.io/twitter/follow/dojostarknet?style=social"/>
</a>
<a href="https://github.com/dojoengine/dojo">
<img src="https://img.shields.io/github/stars/dojoengine/dojo?style=social"/>
</a>

[![discord](https://img.shields.io/badge/join-dojo-green?logo=discord&logoColor=white)](https://discord.gg/PwDa2mKhR4)
[![Telegram Chat][tg-badge]][tg-url]

[tg-badge]: https://img.shields.io/endpoint?color=neon&logo=telegram&label=chat&style=flat-square&url=https%3A%2F%2Ftg.sumanjay.workers.dev%2Fdojoengine
[tg-url]: https://t.me/dojoengine


# Hello Dojo : an Onchain Game
In this project, I tried to create an on-chain game, which means that the entire game logic, assets, and interactions are decentralized and stored on a **blockchain**. This approach offers transparency, security, and unique ownership of in-game items or assets, ultimately revolutionizing how we play and experience games in the digital world.

## Basic Overview
We will be using **Dojo Game Engine**, Dojo is a provable game engine and toolchain for building onchain games and autonomous worlds. Dojo 

---

# How To Start
In this section, I will just give you a quick setup, I highly recommand reading the official documentations, you will find it at the last section of this ReadMe file.

## Installing the requirements
1. **Install Scarb**
    - First you need to have Scarb, Scarb is Cairo Package Manger it's heavily inspired by cargo so you get the idea (I hope XD), you can simply install it by running `curl --proto '=https' --tlsv1.2 -sSf https://docs.swmansion.com/scarb/install.sh | sh`

    - Scarb will set up everything you will need to run your project, If you will use vscode make sure to go to your settings > search for cairo > and enable Scarb 

    - If you have any errors like 
    ```
    error: compiler plugin could not be loaded `dojo_plugin v0.3.0-rc8 (git+https://github.com/dojoengine/dojo)
    ```

    you can simply run `dojoup -v 0.2.3` and replace the old dependecies in `Scrab.toml` with 
    ```
    [dependencies]
    dojo = { git = "https://github.com/dojoengine/dojo.git", tag = "v0.2.3" }
    ```

## Conclusion
I think I mentioned everything you need to know before starting working on this project, now you can jump to the next section and start working on **Hello Dojo** ! 

---

# Dojo Starter: Official Guide

The official Dojo Starter guide, the quickest and most streamlined way to get your Dojo Autonomous World up and running. This guide will assist you with the initial setup, from cloning the repository to deploying your world.

Read the full tutorial [here](https://book.dojoengine.org/cairo/hello-dojo.html)

---

## Contribution

This starter project is a constant work in progress and contributions are greatly appreciated!

1. **Report a Bug**

    - If you think you have encountered a bug, and we should know about it, feel free to report it [here](https://github.com/dojoengine/dojo-starter/issues) and we will take care of it.

2. **Request a Feature**

    - You can also request for a feature [here](https://github.com/dojoengine/dojo-starter/issues), and if it's viable, it will be picked for development.

3. **Create a Pull Request**
    - It can't get better then this, your pull request will be appreciated by the community.

For any other questions, feel free to reach out to us [here](https://dojoengine.org/contact).

Happy coding!
