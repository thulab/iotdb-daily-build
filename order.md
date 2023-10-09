## job下判断：两者都
```
      - name: download & unpack & install -> boost
        if: ${{ matrix.os == 'windows-2022' && matrix.iotdb_version != 'master' }}
        shell: cmd
        run: |
          whoami
          whoami
          whoami
```