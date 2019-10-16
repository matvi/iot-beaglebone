import { Component, OnInit, Input } from '@angular/core';
import { SocketService } from '../_sevices/socket.service';
import * as io from 'socket.io-client';

@Component({
  selector: 'app-temperature',
  templateUrl: './temperature.component.html',
  styleUrls: ['./temperature.component.css']
})
export class TemperatureComponent implements OnInit {

  private socketio: SocketIOClient.Socket;
  public temperature: string;
  public humidity: string;

   @Input() color: string;


  constructor(private socket: SocketService) { }

  ngOnInit() {
    this.connect();
    this.setReceiveMethod();
    this.socket.iniServerSocket();
  }

  connect(){
    this.socketio = io('http://10.42.0.19:5000');
  }

  setReceiveMethod() {
    this.socketio.on('data-tmp', (data) => {
      console.log(data);
      this.temperature = data.temperature + '°C';
      this.humidity = data.humedity;
      this.color = this.getTempColor(data.temperature);
    });
  }

  sendmessage() {
    this.socketio.emit('new-message', 'Hi-flask');
    
  }

  getTempColor(temperature: number) {
    if (temperature < 10 ) {
      return '#334FFF';
    } else if (temperature >= 10 && temperature < 18) {
      return '#33BDFF';
    } else if (temperature >= 18 && temperature < 25) {
      return '#4CFF33';
    } else if (temperature >= 25 && temperature < 32) {
      return '#FFA533';
    } else if (temperature >= 32) {
      return '#F90000';
    }
  }

}
